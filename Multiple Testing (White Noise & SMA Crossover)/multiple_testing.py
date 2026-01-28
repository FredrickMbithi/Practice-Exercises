import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp

def generate_price_series(length=1000, start_price=100, mu=0, sigma=0.01):
    """Generate a random price series using white noise returns."""
    returns = np.random.normal(mu, sigma, length)
    prices = start_price * np.cumprod(1 + returns)
    return pd.Series(prices)

def backtest_sma_crossover(prices, short_window=50, long_window=200):
    """Backtest SMA crossover strategy: buy when short MA > long MA, else sell/hold cash."""
    signals = pd.Series(index=prices.index, dtype=int)
    signals[:] = 0

    short_ma = prices.rolling(short_window).mean()
    long_ma = prices.rolling(long_window).mean()

    # Signal: 1 if short > long, else 0 (hold cash)
    signals[short_ma > long_ma] = 1
    signals[short_ma <= long_ma] = 0

    # Strategy returns: hold asset when signal=1, else cash (0 return)
    strategy_returns = signals.shift(1) * prices.pct_change()

    # Cumulative strategy return
    cum_return = (1 + strategy_returns).cumprod() - 1
    strat_return = cum_return.iloc[-1]

    # Buy-and-hold return for comparison
    bh_return = (prices.iloc[-1] / prices.iloc[0]) - 1

    # P-value: t-test on strategy returns vs 0 (null: no edge)
    clean_returns = strategy_returns.dropna()
    if len(clean_returns) > 0:
        t_stat, p_value = ttest_1samp(clean_returns, 0)
    else:
        p_value = 1.0

    return strat_return, p_value, bh_return

# Main simulation
np.random.seed(42)  # For reproducibility
num_series = 100
results = []

for i in range(num_series):
    prices = generate_price_series()
    strat_ret, p_val, bh_ret = backtest_sma_crossover(prices)
    results.append((strat_ret, p_val, bh_ret))

# Count significant results
alpha = 0.05
significant_count = sum(1 for _, p, _ in results if p < alpha)

# Bonferroni correction
bonferroni_alpha = alpha / num_series
bonferroni_survivors = sum(1 for _, p, _ in results if p < bonferroni_alpha)

print(f"Number of series with p < {alpha}: {significant_count}")
print(f"Bonferroni-corrected alpha: {bonferroni_alpha:.6f}")
print(f"Number of survivors after Bonferroni: {bonferroni_survivors}")

# Optional: Summary stats
strat_rets = [r[0] for r in results]
p_vals = [r[1] for r in results]
bh_rets = [r[2] for r in results]

print(f"\nAverage strategy return: {np.mean(strat_rets):.4f}")
print(f"Average buy-and-hold return: {np.mean(bh_rets):.4f}")
print(f"Average p-value: {np.mean(p_vals):.4f}")