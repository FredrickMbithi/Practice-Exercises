# Multiple Testing: White Noise & SMA Crossover

This project demonstrates the multiple testing problem in quantitative finance by simulating 100 random price series (white noise) and backtesting a simple moving average (SMA) crossover strategy on each.

## Methodology

1. **Generate Price Series**: 100 random walks starting at $100, with daily returns ~ N(0, 0.01²) (white noise, no drift).
2. **SMA Crossover Strategy**: 50-day short MA vs. 200-day long MA. Buy (hold asset) when short > long, else hold cash.
3. **Backtest**: Calculate strategy returns and p-value (t-test: strategy returns vs. 0).
4. **Significance Count**: Count series with p < 0.05.
5. **Bonferroni Correction**: Adjust alpha to 0.05/100 = 0.0005, count survivors.

## Key Findings

- **Significant Results (p < 0.05)**: 9 out of 100 series (9%). This matches the expected ~5% false positive rate under the null hypothesis (random strategy has no edge).
- **Bonferroni Survivors**: 0 out of 100. After correction, no "significant" results remain, highlighting the risk of false discoveries in multiple testing.
- **Average Strategy Return**: -0.0150 (slightly negative, as expected for a random strategy on white noise).
- **Average Buy-and-Hold Return**: 0.0120 (near zero, consistent with no drift).
- **Average P-Value**: 0.5177 (centered around 0.5, indicating no systematic edge).

This illustrates the multiple testing fallacy: without correction, random noise can produce "statistically significant" results by chance. Bonferroni correction mitigates this but may be overly conservative.

## Files

- `multiple_testing.py`: Python script for simulation and backtest.
- `README.md`: This file.

## Requirements

- Python 3.x
- Libraries: numpy, pandas, scipy

## How to Run

1. Install dependencies: `pip install numpy pandas scipy`
2. Run the script: `python multiple_testing.py`

Results are printed to the console.
