# Transaction Costs: Strategy from GitHub

This project demonstrates the impact of transaction costs on a trading strategy. The strategy is a dual moving average crossover (short 100-day MA vs. long 300-day MA) adapted from the public GitHub repository [quantopian/zipline](https://github.com/quantopian/zipline) (file: `zipline/examples/dual_moving_average.py`).

## Methodology

1. **Strategy**: Buy AAPL when 100-day MA > 300-day MA, sell when 100-day MA <= 300-day MA.
2. **Data**: AAPL daily close prices from 2011-01-01 to 2013-01-01.
3. **Backtest**: Simulate trades with starting capital $10,000.
4. **Costs Added**:
   - Bid-ask spread: 0.02% (half on buy/sell).
   - Commission: $0.005/share.
   - Slippage: 0.03% per trade (price impact).
5. **Comparison**: Strategy returns vs. buy-and-hold.

## Key Findings

- **Strategy Final Value**: $9,444.67 (Return: -5.55%)
- **Buy-and-Hold Final Value**: $9,451.60 (Return: -5.48%)
- **Number of Trades**: 1 (Bought 586 shares on 2012-03-13, held to end; no sell signal).
- **Cost Impact**: Transaction costs reduced strategy returns by ~$7 compared to buy-and-hold, but the strategy underperformed BH anyway due to poor timing.

In this case, costs had minimal impact since there was only one trade. In high-frequency strategies, costs would erode returns significantly more.

## Files

- `transaction_costs.py`: Python script for backtest with costs.
- `README.md`: This file.

## Requirements

- Python 3.x
- Libraries: yfinance, pandas, numpy

## How to Run

1. Install dependencies: `pip install yfinance pandas numpy`
2. Run the script: `python transaction_costs.py`

Results are printed to the console.
