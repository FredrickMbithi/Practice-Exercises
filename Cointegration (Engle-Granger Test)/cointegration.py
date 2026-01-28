import yfinance as yf
import pandas as pd
from statsmodels.tsa.stattools import coint

# Tickers to download
tickers = ['SPY', 'IVV', 'XLE', 'XOP', 'GLD', 'GDX']

# Download data
data = yf.download(tickers, start='2010-01-01', end='2026-01-28')['Close']

# Pairs to test
pairs = [('SPY', 'IVV'), ('XLE', 'XOP'), ('GLD', 'GDX')]

print("Cointegration Test Results (Engle-Granger Test)")
print("=" * 50)

for pair in pairs:
    ticker1, ticker2 = pair
    series1 = data[ticker1].dropna()
    series2 = data[ticker2].dropna()

    # Ensure same length
    min_len = min(len(series1), len(series2))
    series1 = series1[-min_len:]
    series2 = series2[-min_len:]

    # Perform cointegration test
    coint_t, p_value, crit_values = coint(series1, series2)

    print(f"\nPair: {ticker1} vs {ticker2}")
    print(f"Cointegration t-statistic: {coint_t:.4f}")
    print(f"P-value: {p_value:.4f}")
    print("Critical values:")
    print(f"  1%: {crit_values[0]:.4f}")
    print(f"  5%: {crit_values[1]:.4f}")
    print(f"  10%: {crit_values[2]:.4f}")

    # Interpretation
    if p_value < 0.05:
        print("Result: Cointegrated (reject null hypothesis of no cointegration)")
    else:
        print("Result: Not cointegrated (fail to reject null)")

print("\nNote: Engle-Granger test null hypothesis is no cointegration. Low p-value indicates cointegration.")