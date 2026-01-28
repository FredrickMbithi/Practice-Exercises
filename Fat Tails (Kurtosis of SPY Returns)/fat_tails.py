import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import kurtosis
import matplotlib.pyplot as plt

# Download SPY daily price data from Yahoo Finance
spy = yf.download('SPY', start='1993-01-01', end='2026-01-28')  # SPY started in 1993

# Calculate daily returns
spy['Return'] = spy['Close'].pct_change()

# Compute rolling 252-day kurtosis (approximately 1 year of trading days)
spy['Kurtosis'] = spy['Return'].rolling(window=252).apply(lambda x: kurtosis(x, fisher=True), raw=False)

# Plot kurtosis over time
plt.figure(figsize=(14, 7))
plt.plot(spy.index, spy['Kurtosis'], label='Rolling 252-day Kurtosis')
plt.axhline(y=3, color='red', linestyle='--', label='Normal Kurtosis Threshold (3)')
plt.title('Rolling 252-day Kurtosis of SPY Daily Returns')
plt.xlabel('Date')
plt.ylabel('Kurtosis')
plt.legend()
plt.savefig('kurtosis_plot.png')
plt.close()  # Close the figure to free memory

# Identify spikes: Kurtosis > 5 (arbitrary threshold for fat tails)
spikes = spy[spy['Kurtosis'] > 5]
print("Spikes in Kurtosis (>5):")
print(spikes[['Kurtosis']].head(20))  # Show first 20 spikes

# For research, we can look up the dates manually or use web search
# Example: For each spike date, research market events