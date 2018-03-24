import statistics
import functools
import operator
import math
import datetime


# timeframe: 1-hour
def ts_to_str(ts):
    ts_string = str(datetime.datetime.fromtimestamp(ts))
    return ts_string.replace(' ', 'T')
    # return ts_string.split()[0]


def __kelly(profits, f=10.0):
    N = len(profits)
    v = 0.0

    for profit in profits:
        profit = profit - 1.0 if profit > 0.0 else 1.0 - profit
        v += (1/N) * math.log10(1+f*profit)

    return v


def get_kelly_ratio(profits):
    candidate = []
    for i in range(1800):
        f = 0.01*i
        try:
            k = __kelly(profits, f)
        except ValueError:
            break
        candidate.append((f, k))
    candidate = sorted(candidate, key=operator.itemgetter(1), reverse=True)

    return candidate[0][0]


def drawdown(data, leverage=1.0):
    net_profit = 1.0
    max_profit = 1.0
    dd = []
    for v in data:
        ts, profit = v

        if profit > 1.0:
            net_profit *= 1.0 + (profit - 1.0) * leverage
        else:
            net_profit *= 1.0 - (1.0 - profit) * leverage

        assert net_profit > 0.0

        if net_profit > max_profit:
            max_profit = net_profit
        dd.append((ts, (net_profit - max_profit) / max_profit))
    return dd, net_profit


class BreakoutDaily():
    def __init__(self, profit_data):
        self.profit_data = profit_data
        self.summary = {}

    def analyze(self):
        for pair in self.profit_data:
            result = self.profit_data[pair]
            for idx in result:
                data = result[idx]
                dd, net_profit = drawdown(data)
                mdd = min([v[1] for v in dd])
                kelly_ratio = get_kelly_ratio([v[1] for v in data])
                kelly_dd, kelly_net_profit = drawdown(data, kelly_ratio)
                kelly_mdd = min([v[1] for v in kelly_dd])
                start_time = data[0][0]
                end_time = data[-1][0]

                if pair not in self.summary:
                    self.summary[pair] = {}

                assert idx not in self.summary[pair]
                self.summary[pair][idx] = {}
                self.summary[pair][idx]['net_profit'] = net_profit
                self.summary[pair][idx]['dd'] = dd
                self.summary[pair][idx]['mdd'] = mdd
                self.summary[pair][idx]['kelly_ratio'] = kelly_ratio
                self.summary[pair][idx]['kelly_net_profit'] = kelly_net_profit
                self.summary[pair][idx]['kelly_mdd'] = kelly_mdd
                self.summary[pair][idx]['start_time'] = start_time
                self.summary[pair][idx]['end_time'] = end_time

                assert ((start_time / 3600) % 24) == ((end_time / 3600) % 24)
                print('[%10s][%s-%s] net_profit: %6.2f, mdd: %6.2f, trades: %4d, min_profit: %4.2f, max_profit: %4.2f' % (
                    pair, ts_to_str(start_time), ts_to_str(end_time),
                    net_profit, mdd, len(data),
                    min([v[1] for v in data]),
                    max([v[1] for v in data])))

    def generate_portfolio(self):
        pass

    def print_summary(self):

        profit_bucket = {}
        for pair in self.summary:
            for idx in self.summary[pair]:
                if idx not in profit_bucket:
                    profit_bucket[idx] = []
                profit = self.summary[pair][idx]['net_profit']
                profit_bucket[idx].append(profit)

        print()
        print('Profit summary for each timeframe.')
        for idx in sorted(profit_bucket.keys()):
            print('%2d: mean: %6.2f, max: %6.2f, min: %6.2f' % (
                idx, statistics.mean(profit_bucket[idx]),
                max(profit_bucket[idx]), min(profit_bucket[idx])))

        print()
        print('Net profit for each cryptocurrency.')
        portfolio_profit = []
        for pair in self.summary:
            mean_mdd = statistics.mean([v['mdd'] for v in self.summary[pair].values()])
            mean_net_profit = statistics.mean([v['net_profit'] for v in self.summary[pair].values()])
            portfolio_profit.append(mean_net_profit)
            print('[%10s] net_profit: %.3f, mdd: %.2f' % (pair, mean_net_profit, mean_mdd))

        print('\nPortfolio profit: %.3f' % statistics.mean(portfolio_profit))
