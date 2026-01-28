# Order Book: Level 2 Data Observation

This exercise involves observing real-time Level 2 order book data for a liquid stock to understand market microstructure. Since this requires live market access, we'll provide instructions for observation and key insights to note.

## Methodology

1. **Tool**: Use a brokerage platform with Level 2 data (e.g., Thinkorswim, Interactive Brokers, or free tools like NASDAQ TotalView).
2. **Stock**: Choose a highly liquid stock like AAPL, TSLA, or SPY.
3. **Duration**: Observe for 10 minutes during market hours (e.g., 9:30-4:00 ET).
4. **What to Observe**:
   - **Spread Changes**: Bid-ask spread fluctuations (tightens/widens).
   - **Order Flow**: Orders appearing/disappearing at different levels.
   - **Large Orders**: Impact of market/limit orders on price movement.
   - **Depth**: Volume at each price level.

## Key Insights

- **Spread Dynamics**: Spreads narrow during high volume, widen during low liquidity or news events. Bid-ask bounce creates noise.
- **Order Book Depth**: Thin books lead to larger price swings from small orders. Iceberg orders hide large volumes.
- **Price Impact**: Large orders can "walk the book," pushing prices. HFTs provide liquidity but add slippage.
- **Backtest Implications**: Real trading faces slippage, queue position, and adverse selection. Backtests assuming instant execution at mid-price are unrealistic.

## Instructions

1. Log into a platform with Level 2 access.
2. Select a liquid stock and view the order book.
3. Note changes every minute for 10 minutes.
4. Record observations on spread, order flow, and price impacts.

This highlights why transaction costs and slippage must be modeled accurately in backtests.

## Files

- `README.md`: This file (no script needed for observation).

## Requirements

- Access to Level 2 data (brokerage account or demo).
- Market hours observation.

## Example Observations

- Spread: Starts at $0.01, widens to $0.05 during news.
- Orders: Small orders flicker, large buy order lifts multiple levels.
- Impact: 10,000 share order moves price up $0.02.
