# This file downloads Stock prices

import yfinance as yf

tickers = ["SPY", "QQQM", "TLT"]
data = {}

for ticker in tickers:
    stock_data = yf.Ticker(ticker)
    data[ticker] = stock_data.history(period="1y")['Close']
