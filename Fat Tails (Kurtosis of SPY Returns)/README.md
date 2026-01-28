# Fat Tails: Kurtosis Analysis of SPY Returns

This project analyzes the fat tails in SPY (S&P 500 ETF) daily returns by computing rolling 252-day kurtosis over time. Kurtosis measures the "tailedness" of the return distribution; values above 3 indicate fat tails (more extreme events than a normal distribution).

## Methodology

1. **Data Download**: SPY daily price data from 1993-01-01 to 2026-01-28 using Yahoo Finance.
2. **Returns Calculation**: Daily percentage returns from adjusted close prices.
3. **Rolling Kurtosis**: 252-day (approximately 1 year) rolling window kurtosis using Fisher's definition (excess kurtosis).
4. **Plotting**: Time series plot of kurtosis with a red line at 3 (normal threshold).
5. **Spike Identification**: Days where kurtosis > 5, indicating significant fat tails.

## Key Findings

- **Spikes in Kurtosis**: 1,169 days with kurtosis > 5 from 1997-10-27 to 2026-01-27. The earliest and most prominent spikes (kurtosis ~5.3 to 6.2) occurred in October-November 1997.
- **Market Events During Spikes**: These align with the **1997 Asian Financial Crisis**:
  - Started in July 1997 with Thailand's baht devaluation due to speculative attacks and low foreign reserves.
  - Spread to Indonesia, South Korea, Malaysia, Philippines, etc., causing currency depreciations (e.g., Indonesian rupiah fell 83%, South Korean won 34%).
  - Stock markets crashed (e.g., Hong Kong Hang Seng -23% in October 1997).
  - Causes: Over-leveraged economies, fixed exchange rates, hot money inflows, asset bubbles, and crony capitalism.
  - Global impact: U.S. Dow Jones -7.2% on October 27, 1997; IMF bailouts ($118B) led to recessions (e.g., Indonesia GDP -13.1% in 1998).
- **Later Spikes**: High kurtosis during other crises like 2008-2009 (Global Financial Crisis: housing bubble, subprime mortgages, bank failures).

The plot (`kurtosis_plot.png`) shows kurtosis frequently exceeding 3 during volatile periods, highlighting non-normal return behavior.

## Files

- `fat_tails.py`: Python script for analysis.
- `kurtosis_plot.png`: Plot of rolling kurtosis.
- `README.md`: This file.

## Requirements

- Python 3.x
- Libraries: yfinance, pandas, numpy, scipy, matplotlib

## How to Run

1. Install dependencies: `pip install yfinance pandas numpy scipy matplotlib`
2. Run the script: `python fat_tails.py`

The script saves the plot and prints spike details to the console.
