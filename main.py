#!/usr/bin/env python3
import sys
from backtest import strategy, portfolio

if __name__ == "__main__":
    if len(sys.argv) < 2:
        dataset_path = './market_data/upbit.candles.csv'
    else:
        dataset_path = sys.argv[1]

    upbit_krw_markets = [
            'BTC', 'ADA', 'QTUM', 'XEM', 'XRP', 'SNT', 'ETH',
            'NEO', 'ETC', 'XLM', 'BCC', 'EMC2', 'SBD', 'MER',
            'BTG', 'STEEM', 'LTC', 'OMG', 'LSK', 'TIX', 'POWR',
            'ARDR', 'MTL', 'STORJ', 'GRS', 'STRAT', 'KMD',
            'ARK', 'REP', 'XMR', 'DASH', 'WAVES', 'VTC', 'PIVX', 'ZEC']

    breakout = strategy.Breakout()
    breakout.load_dataset(dataset_path)
    breakout.set_market('KRW')
    breakout.set_currencies(upbit_krw_markets)

    profit_summary = breakout.backtest(
            fee=0.0015,
            breakout_coefficient=0.5,
            risk_mgmt=0.05,
            ma_filtering=True,
            noise_filtering=False,
            adaptive_coeff=False,
            timeframe_distribution=True)

    pf = portfolio.BreakoutDaily(profit_summary)
    pf.analyze()
    pf.print_summary()
