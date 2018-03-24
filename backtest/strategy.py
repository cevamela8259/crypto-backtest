import pprint
import statistics
import operator
import functools
import datetime
import time

# timeframe: 1-hour
def ts_to_str(ts):
    ts_string = str(datetime.datetime.fromtimestamp(ts))
    return ts_string.replace(' ', 'T')
    # return ts_string.split()[0]

class Breakout():
    def __init__(self):
        self.data = {}
        self.markets = []
        self.currencies = []

    def set_market(self, markets):
        self.markets = markets

    def set_currencies(self, currencies):
        self.currencies = currencies

    def load_dataset(self, dataset_path):
        with open(dataset_path, 'r') as fp:
            for line in fp:
                orig_line = line
                line = line.strip().split(',')
                exchange = line[0]
                # the base currency represents how much of the quote currency
                # is needed for you to get one unit of the base currency
                base_symbol = line[1]
                quote_symbol = line[2]
                timestamp = int(line[3]) # in seconds
                timeframe = int(line[4])
                O = float(line[5])
                H = float(line[6])
                L = float(line[7])
                C = float(line[8])
                BV = float(line[9])
                # QV = float(line[10])
                if quote_symbol not in self.data:
                    self.data[quote_symbol] = {}
                if base_symbol not in self.data[quote_symbol]:
                    self.data[quote_symbol][base_symbol] = []
                self.data[quote_symbol][base_symbol].append(
                        (timestamp, timeframe, O, H, L, C, BV))

        # sort and remove duplicated rows in the dataset
        for quote_symbol in self.data:
            for base_symbol in self.data[quote_symbol]:
                v = sorted(self.data[quote_symbol][base_symbol])
                dup_indexes = []
                cnt = 0
                tmp = [v[0]]
                for i in range(len(v)):
                    if i == 0:
                        continue
                    if (v[i][0] != v[i-1][0]):
                        tmp.append(v[i])
                for i in range(len(tmp)):
                    if i == 0:
                        continue
                    assert(tmp[i][0] != v[i-1][0])
                self.data[quote_symbol][base_symbol] = tmp


    def __candle(self, start_time, chunk):
        assert len(chunk) <= 24
        ts = start_time
        tf = chunk[0][1]
        O = chunk[0][2]
        H = max([v[3] for v in chunk])
        L = min([v[4] for v in chunk])
        C = chunk[-1][5]
        V = sum([v[6] for v in chunk])
        # print([ts_to_str(ts), tf, O, H, L, C, V])

        assert H >= O
        assert H >= L
        assert H >= C
        assert L <= O
        assert L <= H
        assert L <= C

        return (ts, tf, O, H, L, C, V)

    def __preprocessing(self, data):
        shifted_data = {}

        i = 0
        # split the dataset into different timeframes by shifting
        while True:
            ts = data[i][0]
            ts = ts - (ts % 3600)
            idx = (ts / 3600) % 24
            if len(shifted_data.keys()) == 24:
                break
            if idx not in shifted_data:
                shifted_data[idx] = data[i:]
            i += 1

        # generate daily candles using the shifted hourly candles
        shifted_candle = {}
        for idx in sorted(shifted_data.keys()):
            shifted_candle[idx] = []
            chunk = []
            ts = shifted_data[idx][0][0]
            start_time = ts - (ts % 3600)
            assert (start_time / 3600) % 24 == idx
            for i, row in enumerate(shifted_data[idx]):
                if shifted_data[idx][i][0] >= start_time + 3600 * 24:
                    # emit a chunk
                    candle = self.__candle(start_time, chunk)
                    shifted_candle[idx].append(candle)
                    chunk = [shifted_data[idx][i]]
                    start_time = start_time + 3600 * 24
                    assert (start_time / 3600) % 24 == idx
                else:
                    chunk.append(shifted_data[idx][i])

        for idx in sorted(shifted_candle.keys()):
            for i in range(len(shifted_candle[idx])):
                if i == 0:
                    continue
                assert (shifted_candle[idx][i-1][0] + 86400) == shifted_candle[idx][i][0]
        self.shifted_candle = shifted_candle

    def __breakout(self, name, fee=0.0015, breakout_coefficient=0.05,
            risk_mgmt=0.05, ma_filtering=True, noise_filtering=True,
            adaptive_coeff=True, timeframe_distribution=True):

        # configuration parameters
        ma_periods = 5
        noise_periods = 20
        noise_filtering_threshold = 0.6
        default_timeframe = 0

        profits = {}
        for idx in sorted(self.shifted_candle.keys()):
            if not timeframe_distribution:
                idx = default_timeframe

            profits[idx] = []
            for i, row in enumerate(self.shifted_candle[idx]):
                if i == 0:
                    continue
                if ma_filtering and (i < ma_periods):
                    continue
                if (noise_filtering or adaptive_coeff) and (i < noise_periods):
                    continue

                row_yday = self.shifted_candle[idx][i-1]
                row_tday = self.shifted_candle[idx][i]
                ts_yday, tf_yday, O_yday, H_yday, L_yday, C_yday, V_yday = row_yday
                ts_tday, tf_tday, O_tday, H_tday, L_tday, C_tday, V_tday = row_tday

                if ma_filtering:
                    ma_price = [v[5] for v in self.shifted_candle[idx][i-ma_periods:i]]
                    ma_price = statistics.mean(ma_price)

                # skip this day if the closing price of yesterday is lower than
                # the moving average.
                if ma_filtering and (C_yday < ma_price):
                    continue
                
                if noise_filtering or adaptive_coeff:
                    ma_noise = []
                    for v in self.shifted_candle[idx][i-noise_periods:i]:
                        if (v[3] - v[4]) == 0.0:
                            noise = 0.5
                        else:
                            noise = 1 - abs(v[2] - v[5]) / (v[3] - v[4])
                        ma_noise.append(noise)
                    ma_noise = statistics.mean(ma_noise)

                # skip this day if the average noise of recent days is
                # higher than the noise_filtering_threshold.
                if noise_filtering and (ma_noise > noise_filtering_threshold):
                    continue

                if adaptive_coeff:
                    # use the average noise of recent days for the breakout
                    # coefficient.
                    threshold = ma_noise * (H_yday - L_yday) + O_tday
                else:
                    threshold = breakout_coefficient * (H_yday - L_yday) + O_tday

                if (L_yday - H_yday) == 0.0:
                    x = 1.0
                else:
                    # trying to limit the maximum loss of this trade using
                    # the range of the yesterday.
                    x = risk_mgmt / abs((L_yday - H_yday) / H_yday)
                    x = 1.0 if x > 1.0 else x

                if H_tday > threshold:
                    buy_price = threshold * (1+fee)
                    sell_price = C_tday * (1-fee)
                    profit = (sell_price - buy_price) / buy_price
                    profit *= x
                    profits[idx].append((ts_yday, 1+profit))
            
            # terminate the loop here if timeframe_distribution is disabled.
            if not timeframe_distribution:
                break

        return profits

    def backtest(self, fee=0.0015, breakout_coefficient=0.5, risk_mgmt=0.05,
            ma_filtering=True, noise_filtering=True,
            adaptive_coeff=True, timeframe_distribution=True):
        result = {}
        for quote_symbol in self.data:
            for base_symbol in self.data[quote_symbol]:
                if (self.markets != []) and (quote_symbol not in self.markets):
                    continue
                if (self.currencies != []) and (base_symbol not in self.currencies):
                    continue
                print('%s-%s' % (base_symbol, quote_symbol))

                data = self.data[quote_symbol][base_symbol]

                # we need at least 72 hourly candles for timeframe distribution
                if len(data) < 24*3:
                    # print('[%s-%s] error not enough data points: %d' % (
                        # base_symbol, quote_symbol, len(data)))
                    continue
                # print('[%s-%s] data points: %d' % (
                    # base_symbol, quote_symbol, len(data)))

                self.__preprocessing(data)
                profits = self.__breakout(
                        '%s-%s' % (base_symbol, quote_symbol), fee,
                        breakout_coefficient, risk_mgmt, ma_filtering,
                        noise_filtering, adaptive_coeff, timeframe_distribution)

                if any([len(profits[idx]) == 0 for idx in profits]):
                    print('%s-%s: 0 trades, do not include it in the result.' % (
                        base_symbol, quote_symbol))
                    continue
                result['%s-%s' % (base_symbol, quote_symbol)] = profits

        return result