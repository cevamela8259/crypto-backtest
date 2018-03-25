# crypto-backtest

## How to use

### 1. Prepare dataset.
```
$ cd market_data
$ tar xvfz binance.candles.csv.tar.gz
$ tar xvfz bitfinex.candles.csv.tar.gz
$ tar xvfz bitmex.candles.csv.tar.gz
$ tar xvfz upbit.candles.csv.tar.gz
$ cd ..
```

### 2. Run a backtest
```
$ ./test.py market_data/upbit.candles.csv
```

### 3. Example result
```
BTC-KRW
ETH-KRW
[   BTC-KRW][2017-09-30T09:00:00-2018-03-19T09:00:00] net_profit:   1.66, mdd:  -0.06, trades:   45, min_profit: 0.95, max_profit: 1.08
[   BTC-KRW][2017-09-29T10:00:00-2018-03-19T10:00:00] net_profit:   1.65, mdd:  -0.09, trades:   54, min_profit: 0.94, max_profit: 1.10
[   BTC-KRW][2017-09-29T11:00:00-2018-03-19T11:00:00] net_profit:   1.51, mdd:  -0.11, trades:   55, min_profit: 0.94, max_profit: 1.09
[   BTC-KRW][2017-09-29T12:00:00-2018-03-19T12:00:00] net_profit:   1.37, mdd:  -0.12, trades:   55, min_profit: 0.94, max_profit: 1.10
[   BTC-KRW][2017-09-29T13:00:00-2018-03-19T13:00:00] net_profit:   1.38, mdd:  -0.11, trades:   55, min_profit: 0.94, max_profit: 1.07
[   BTC-KRW][2017-09-29T14:00:00-2018-03-19T14:00:00] net_profit:   1.45, mdd:  -0.09, trades:   51, min_profit: 0.94, max_profit: 1.06
[   BTC-KRW][2017-09-29T15:00:00-2018-03-19T15:00:00] net_profit:   1.37, mdd:  -0.12, trades:   54, min_profit: 0.94, max_profit: 1.08
[   BTC-KRW][2017-09-29T16:00:00-2018-03-19T16:00:00] net_profit:   1.32, mdd:  -0.13, trades:   58, min_profit: 0.94, max_profit: 1.10
[   BTC-KRW][2017-09-29T17:00:00-2018-03-19T17:00:00] net_profit:   1.33, mdd:  -0.14, trades:   53, min_profit: 0.94, max_profit: 1.08
[   BTC-KRW][2017-09-29T18:00:00-2018-03-19T18:00:00] net_profit:   1.31, mdd:  -0.13, trades:   56, min_profit: 0.94, max_profit: 1.09
[   BTC-KRW][2017-09-29T19:00:00-2018-03-19T19:00:00] net_profit:   1.22, mdd:  -0.19, trades:   56, min_profit: 0.94, max_profit: 1.10
[   BTC-KRW][2017-09-29T20:00:00-2018-03-01T20:00:00] net_profit:   1.41, mdd:  -0.15, trades:   50, min_profit: 0.94, max_profit: 1.09
[   BTC-KRW][2017-09-30T21:00:00-2018-03-01T21:00:00] net_profit:   1.21, mdd:  -0.15, trades:   51, min_profit: 0.94, max_profit: 1.11
[   BTC-KRW][2017-09-30T22:00:00-2018-03-18T22:00:00] net_profit:   1.42, mdd:  -0.14, trades:   50, min_profit: 0.94, max_profit: 1.12
[   BTC-KRW][2017-10-05T23:00:00-2018-03-18T23:00:00] net_profit:   1.60, mdd:  -0.07, trades:   45, min_profit: 0.96, max_profit: 1.14
[   BTC-KRW][2017-10-06T00:00:00-2018-03-18T00:00:00] net_profit:   1.67, mdd:  -0.09, trades:   42, min_profit: 0.93, max_profit: 1.13
[   BTC-KRW][2017-10-02T01:00:00-2018-03-18T01:00:00] net_profit:   1.72, mdd:  -0.05, trades:   44, min_profit: 0.96, max_profit: 1.14
[   BTC-KRW][2017-10-02T02:00:00-2018-03-19T02:00:00] net_profit:   1.73, mdd:  -0.16, trades:   52, min_profit: 0.91, max_profit: 1.15
[   BTC-KRW][2017-09-29T03:00:00-2018-03-18T03:00:00] net_profit:   1.68, mdd:  -0.12, trades:   53, min_profit: 0.92, max_profit: 1.16
[   BTC-KRW][2017-09-29T04:00:00-2018-03-18T04:00:00] net_profit:   1.73, mdd:  -0.10, trades:   49, min_profit: 0.91, max_profit: 1.19
[   BTC-KRW][2017-09-30T05:00:00-2018-03-19T05:00:00] net_profit:   1.80, mdd:  -0.08, trades:   44, min_profit: 0.96, max_profit: 1.19
[   BTC-KRW][2017-09-30T06:00:00-2018-03-19T06:00:00] net_profit:   1.57, mdd:  -0.06, trades:   48, min_profit: 0.97, max_profit: 1.12
[   BTC-KRW][2017-09-30T07:00:00-2018-03-19T07:00:00] net_profit:   1.44, mdd:  -0.10, trades:   51, min_profit: 0.94, max_profit: 1.11
[   BTC-KRW][2017-09-29T08:00:00-2018-03-19T08:00:00] net_profit:   1.72, mdd:  -0.10, trades:   51, min_profit: 0.96, max_profit: 1.08
[   ETH-KRW][2017-09-30T09:00:00-2018-02-16T09:00:00] net_profit:   1.37, mdd:  -0.12, trades:   39, min_profit: 0.94, max_profit: 1.20
[   ETH-KRW][2017-09-30T10:00:00-2018-02-18T10:00:00] net_profit:   1.21, mdd:  -0.16, trades:   40, min_profit: 0.93, max_profit: 1.21
[   ETH-KRW][2017-10-05T11:00:00-2018-02-18T11:00:00] net_profit:   1.18, mdd:  -0.19, trades:   43, min_profit: 0.91, max_profit: 1.13
[   ETH-KRW][2017-10-01T12:00:00-2018-02-18T12:00:00] net_profit:   1.25, mdd:  -0.13, trades:   41, min_profit: 0.91, max_profit: 1.12
[   ETH-KRW][2017-09-29T13:00:00-2018-02-18T13:00:00] net_profit:   1.38, mdd:  -0.08, trades:   41, min_profit: 0.95, max_profit: 1.12
[   ETH-KRW][2017-09-29T14:00:00-2018-02-18T14:00:00] net_profit:   0.88, mdd:  -0.47, trades:   41, min_profit: 0.54, max_profit: 1.17
[   ETH-KRW][2017-09-29T15:00:00-2018-02-18T15:00:00] net_profit:   0.74, mdd:  -0.47, trades:   41, min_profit: 0.54, max_profit: 1.19
[   ETH-KRW][2017-09-29T16:00:00-2018-02-18T16:00:00] net_profit:   0.65, mdd:  -0.53, trades:   40, min_profit: 0.54, max_profit: 1.18
[   ETH-KRW][2017-10-01T17:00:00-2018-03-19T17:00:00] net_profit:   1.19, mdd:  -0.13, trades:   44, min_profit: 0.92, max_profit: 1.16
[   ETH-KRW][2017-09-29T18:00:00-2018-03-19T18:00:00] net_profit:   1.57, mdd:  -0.11, trades:   46, min_profit: 0.95, max_profit: 1.16
[   ETH-KRW][2017-10-01T19:00:00-2018-03-19T19:00:00] net_profit:   1.26, mdd:  -0.13, trades:   46, min_profit: 0.95, max_profit: 1.12
[   ETH-KRW][2017-10-01T20:00:00-2018-03-19T20:00:00] net_profit:   1.12, mdd:  -0.12, trades:   42, min_profit: 0.96, max_profit: 1.12
[   ETH-KRW][2017-10-01T21:00:00-2018-03-19T21:00:00] net_profit:   1.05, mdd:  -0.10, trades:   42, min_profit: 0.90, max_profit: 1.11
[   ETH-KRW][2017-10-01T22:00:00-2018-02-18T22:00:00] net_profit:   1.11, mdd:  -0.12, trades:   43, min_profit: 0.95, max_profit: 1.10
[   ETH-KRW][2017-10-01T23:00:00-2018-02-16T23:00:00] net_profit:   1.18, mdd:  -0.11, trades:   42, min_profit: 0.90, max_profit: 1.12
[   ETH-KRW][2017-10-02T00:00:00-2018-02-20T00:00:00] net_profit:   0.83, mdd:  -0.20, trades:   45, min_profit: 0.84, max_profit: 1.08
[   ETH-KRW][2017-10-11T01:00:00-2018-03-20T01:00:00] net_profit:   1.34, mdd:  -0.09, trades:   39, min_profit: 0.92, max_profit: 1.11
[   ETH-KRW][2017-10-02T02:00:00-2018-03-20T02:00:00] net_profit:   1.33, mdd:  -0.08, trades:   43, min_profit: 0.93, max_profit: 1.17
[   ETH-KRW][2017-09-29T03:00:00-2018-03-20T03:00:00] net_profit:   1.48, mdd:  -0.11, trades:   46, min_profit: 0.92, max_profit: 1.19
[   ETH-KRW][2017-09-29T04:00:00-2018-03-20T04:00:00] net_profit:   1.34, mdd:  -0.11, trades:   44, min_profit: 0.93, max_profit: 1.17
[   ETH-KRW][2017-09-30T05:00:00-2018-03-11T05:00:00] net_profit:   1.46, mdd:  -0.13, trades:   43, min_profit: 0.92, max_profit: 1.14
[   ETH-KRW][2017-09-30T06:00:00-2018-02-19T06:00:00] net_profit:   1.34, mdd:  -0.13, trades:   44, min_profit: 0.94, max_profit: 1.18
[   ETH-KRW][2017-10-05T07:00:00-2018-02-16T07:00:00] net_profit:   1.44, mdd:  -0.15, trades:   42, min_profit: 0.93, max_profit: 1.17
[   ETH-KRW][2017-09-30T08:00:00-2018-02-18T08:00:00] net_profit:   1.39, mdd:  -0.15, trades:   45, min_profit: 0.92, max_profit: 1.18

Profit summary for each timeframe.
 0: mean:   1.51, max:   1.66, min:   1.37
 1: mean:   1.43, max:   1.65, min:   1.21
 2: mean:   1.35, max:   1.51, min:   1.18
 3: mean:   1.31, max:   1.37, min:   1.25
 4: mean:   1.38, max:   1.38, min:   1.38
 5: mean:   1.16, max:   1.45, min:   0.88
 6: mean:   1.05, max:   1.37, min:   0.74
 7: mean:   0.99, max:   1.32, min:   0.65
 8: mean:   1.26, max:   1.33, min:   1.19
 9: mean:   1.44, max:   1.57, min:   1.31
10: mean:   1.24, max:   1.26, min:   1.22
11: mean:   1.26, max:   1.41, min:   1.12
12: mean:   1.13, max:   1.21, min:   1.05
13: mean:   1.26, max:   1.42, min:   1.11
14: mean:   1.39, max:   1.60, min:   1.18
15: mean:   1.25, max:   1.67, min:   0.83
16: mean:   1.53, max:   1.72, min:   1.34
17: mean:   1.53, max:   1.73, min:   1.33
18: mean:   1.58, max:   1.68, min:   1.48
19: mean:   1.53, max:   1.73, min:   1.34
20: mean:   1.63, max:   1.80, min:   1.46
21: mean:   1.46, max:   1.57, min:   1.34
22: mean:   1.44, max:   1.44, min:   1.44
23: mean:   1.55, max:   1.72, min:   1.39

Net profit for each cryptocurrency.
[   ETH-KRW] net_profit: 1.213, mdd: -0.17
[   BTC-KRW] net_profit: 1.511, mdd: -0.11

Portfolio profit: 1.362
```
