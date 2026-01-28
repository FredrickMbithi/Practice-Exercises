import yfinance as yf
import pandas as pd
import numpy as np

# Download data for AAPL (as in the zipline example)
ticker = 'AAPL'
data = yf.download(ticker, start='2011-01-01', end='2013-01-01')[('Close', ticker)]

# Strategy parameters
short_window = 100
long_window = 300
capital = 10000  # Starting capital

# Transaction costs
bid_ask_spread = 0.0002  # 0.02%
commission_per_share = 0.005  # $0.005/share
slippage_pct = 0.0003  # 0.03%

# Calculate moving averages
data = pd.Series(data)
short_ma = data.rolling(window=short_window).mean()
long_ma = data.rolling(window=long_window).mean()

# Generate signals
signals = pd.Series(index=data.index, dtype=int)
signals[:] = 0
signals[short_ma > long_ma] = 1
signals[short_ma <= long_ma] = 0

# Backtest with costs
position = 0  # Number of shares
cash = capital
portfolio_value = []
trade_log = []

for i in range(len(data)):
    if i < long_window:  # Skip until we have full windows
        portfolio_value.append(cash)
        continue

    current_price = data.iloc[i]
    signal = signals.iloc[i]

    # Check for trade
    if signal == 1 and position == 0:  # Buy
        # Adjust price for costs
        effective_price = current_price * (1 + bid_ask_spread / 2 + slippage_pct)
        shares_to_buy = int(cash / (effective_price + commission_per_share))
        if shares_to_buy > 0:
            cost = shares_to_buy * (effective_price + commission_per_share)
            cash -= cost
            position = shares_to_buy
            trade_log.append(f"Buy {shares_to_buy} at {effective_price:.2f} on {data.index[i].date}")

    elif signal == 0 and position > 0:  # Sell
        # Adjust price for costs
        effective_price = current_price * (1 - bid_ask_spread / 2 - slippage_pct)
        proceeds = position * (effective_price - commission_per_share)
        cash += proceeds
        trade_log.append(f"Sell {position} at {effective_price:.2f} on {data.index[i].date}")
        position = 0

    # Portfolio value
    portfolio_value.append(cash + position * current_price)

# Buy-and-hold for comparison
bh_shares = int(capital / data.iloc[long_window])
bh_value = capital - (bh_shares * data.iloc[long_window]) + (bh_shares * data.iloc[-1])

# Strategy final value
strategy_final = portfolio_value[-1]

print(f"Strategy Final Portfolio Value: ${strategy_final:.2f}")
print(f"Buy-and-Hold Final Value: ${bh_value:.2f}")
print(f"Strategy Return: {((strategy_final / capital) - 1) * 100:.2f}%")
print(f"Buy-and-Hold Return: {((bh_value / capital) - 1) * 100:.2f}%")
print(f"Number of Trades: {len(trade_log)}")
print("\nSample Trades:")
for trade in trade_log[:5]:  # Show first 5
    print(trade)