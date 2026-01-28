# Cointegration: Engle-Granger Test

This project tests for cointegration between pairs of ETFs using the Engle-Granger test in statsmodels. Cointegration indicates a long-run equilibrium relationship between two time series, even if they diverge short-term.

## Methodology

1. **Data Download**: Daily close prices for SPY, IVV, XLE, XOP, GLD, GDX from 2010-01-01 to 2026-01-28 using Yahoo Finance.
2. **Pairs Tested**:
   - (SPY, IVV): Both track S&P 500 index.
   - (XLE, XOP): Energy sector ETFs (XLE: Energy Select Sector SPDR, XOP: SPDR S&P Oil & Gas Exploration & Production).
   - (GLD, GDX): Gold ETF (GLD) and gold miners ETF (GDX).
3. **Engle-Granger Test**: Regress one series on the other, test residuals for stationarity (ADF test). Null: no cointegration.

## Key Findings

All pairs failed the cointegration test at the 5% significance level (p > 0.05). Results:

- **SPY vs IVV**:
  - t-statistic: -0.3124
  - P-value: 0.9753
  - Critical values: 1% -3.8992, 5% -3.3376, 10% -3.0455
  - Result: Not cointegrated

- **XLE vs XOP**:
  - t-statistic: 0.2121
  - P-value: 0.9898
  - Critical values: 1% -3.8992, 5% -3.3376, 10% -3.0455
  - Result: Not cointegrated

- **GLD vs GDX**:
  - t-statistic: -0.6375
  - P-value: 0.9530
  - Critical values: 1% -3.8992, 5% -3.3376, 10% -3.0455
  - Result: Not cointegrated

## Interpretation

- **SPY and IVV**: Despite tracking the same index, they are not cointegrated, possibly due to slight differences in fees, rebalancing, or tracking errors.
- **XLE and XOP**: Both energy-focused, but XOP is more volatile (exploration/production), leading to no long-run equilibrium.
- **GLD and GDX**: Gold price vs. miners' performance; miners are leveraged to gold prices but affected by operational factors, breaking cointegration.

Cointegration is rare in practice; high correlation doesn't imply cointegration. For pairs trading, further analysis (e.g., error correction models) is needed if cointegration is suspected.

## Files

- `cointegration.py`: Python script for data download and testing.
- `README.md`: This file.

## Requirements

- Python 3.x
- Libraries: yfinance, pandas, statsmodels

## How to Run

1. Install dependencies: `pip install yfinance pandas statsmodels`
2. Run the script: `python cointegration.py`

Results are printed to the console.
