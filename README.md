# Phase 1: Quant Trading Foundations (2-3 Months)

## Deep Educational Guide with Referenced Sources

---

## Part 1: Statistics & Probability

### 1.1 Fat-Tailed Distributions: Why Normal Is Never Normal in Finance

**The Core Problem:**
Most introductory statistics teaches the normal (Gaussian) distribution. Financial markets laugh at this assumption. If the distribution is actually fat-tailed, the Black-Scholes model will under-price options that are far out of the money, since a 5- or 7-sigma event is much more likely than the normal distribution would predict.

**What Are Fat Tails?**
Fat tails indicate a greater likelihood of extreme market events, both positive and negative, compared to normal distributions. In practical terms:

- A 3-sigma event in a normal distribution should occur 0.3% of the time
- In financial markets, these events happen far more frequently
- By definition, fat tails are a statistical phenomenon exhibiting large leptokurtosis, representing a greater likelihood of extreme events occurring similar to the financial crisis

**Measuring Fat Tails - Kurtosis:**
Kurtosis is a measure of the "tailedness" of the probability distribution. Most financial distributions are fat-tailed relative to the normal distribution, with leptokurtic behavior meaning extreme outcomes are more likely than predicted by a normal distribution.

Three types of distributions:

- **Mesokurtic**: Normal distribution (kurtosis ≈ 3)
- **Leptokurtic**: Fat tails (kurtosis > 3) - this is what you see in finance
- **Platykurtic**: Thin tails (kurtosis < 3)

**Real-World Evidence:**
The Korean stock market from 1980 to 2015 showed descriptive statistics with a kurtosis of 8.5081, far exceeding the normal distribution's kurtosis of 3. This means extreme events were nearly 3 times more common than a normal distribution would predict.

**Why This Matters for Backtesting:**
Standard deviations and variance are not useable under fat tails. They fail out of sample, even when they exist. There is no fat tailed distribution in which the mean can be properly estimated directly from the sample mean, unless we have orders of magnitude more data than we do.

This is Nassim Taleb's key insight: your backtest using mean and standard deviation from historical data is likely wrong if you haven't accounted for fat tails. The "safe" 2-standard-deviation move you planned for might actually be a 5-sigma event that wipes you out.

**Practical Implications:**

1. Don't trust Value at Risk (VaR) models based on normal distributions
2. Your max drawdown will be larger than your backtest suggests
3. Position sizing must account for extreme events being more common
4. Stop losses are orders placed to sell a security when it reaches a designated price. Since your position sizing should be based on the distance of your stop from your entry price, exiting a losing trade with a stop loss can help you cut off the ends of those fat tails

---

### 1.2 Multiple Testing Problem: Why 95% of Your "Significant" Strategies Are Flukes

**The Problem:**
You backtest 100 different strategy variations. Twenty of them show statistical significance at p < 0.05. You think you've found 20 profitable strategies. You've actually found noise.

**The Mathematics:**
If m independent comparisons are performed, the family-wise error rate (FWER) increases as the number of comparisons increases. The probability of getting at least one false positive is 1 - (1 - α)^m.

With α = 0.05 and 20 tests:

- Probability of at least one false positive = 1 - (0.95)^20 = 64%

**Real-World Translation:**
If you do 100 statistical tests, and for all of them the null hypothesis is actually true, you'd expect about 5 of the tests to be significant at the P < 0.05 level, just due to chance.

This is why most backtested strategies fail in live trading. You tested 100 variations of moving average crossovers, found 5 that "worked" historically, and deployed them thinking you found edge. You didn't—you found statistical noise.

**The Bonferroni Correction:**
Statistical hypothesis testing is based on rejecting the null hypothesis when the likelihood of the observed data would be low if the null hypothesis were true. The Bonferroni correction compensates for increased false positives by testing each individual hypothesis at α/m, where m is the number of tests.

If testing 100 strategies at α = 0.05:

- Bonferroni-corrected threshold: 0.05/100 = 0.0005
- Only p-values below 0.0005 are considered significant

**The Trade-Off:**
There is an immediate consequence of applying a Bonferroni correction: the probability that a true relation may go unnoticed will increase (type 2 error). In a study in which a single test has a power of 80%, the power of each of 25 Bonferroni corrected tests would be less than 39%.

**Practical Application in Quant Trading:**

1. **Strategy Development**: If you test 50 parameter combinations, your significance threshold should be 0.05/50 = 0.001, not 0.05
2. **Feature Selection**: Testing 100 technical indicators? Only accept p < 0.0005 as meaningful
3. **Alternative Approach**: FDR analysis is appropriate if follow-up analyses will depend upon groups of scores and you're willing to tolerate having a fixed percentage of experiments fail

**Critical Reality Check:**
The roadmap's warning about "most ideas will fail" connects directly here. If you're testing many variations and using p < 0.05 without correction, you're guaranteeing false positives. The Bonferroni correction should be considered if it is imperative to avoid a type I error, and a large number of tests are carried out without preplanned hypotheses.

---

### 1.3 Time Series Concepts: Stationarity, Autocorrelation, and Cointegration

#### Stationarity: The Foundation

**Definition:**
The statistical properties, such as the mean, variance, or autocorrelation, of a stationary time series are independent of the period—they don't change over time. Stationarity implies that a time series does not have a trend or seasonal effects.

**Why It Matters:**
Most statistical models assume stationarity. Asset prices are **not stationary**—they trend, they have volatility regimes, they drift. This breaks most traditional statistical methods.

**Three Conditions for Stationarity:**
A time series can be marked as "Stationary" if it fulfils three statistical conditions: (1) The mean of the series should remain steady, (2) Standard deviation of the series should be within range, (3) There should be no autocorrelation within the series.

**Testing for Stationarity:**
The augmented Dickey-Fuller test (ADF) is an effective way of evaluating the stationarity of a time series. The ADF test carries out all necessary steps and additionally involves a multiple lag process to assess autocorrelation.

#### Autocorrelation: When Today Predicts Tomorrow

**Definition:**
Autocorrelation is defined as the degree of similarity between a given time series and a lagged version of itself—it measures the correlation between the values of a time series at different points in time.

**Practical Meaning:**
If a stock's return today tells you something about tomorrow's return, that's autocorrelation. Mean reversion strategies exploit negative autocorrelation. Momentum strategies exploit positive autocorrelation.

**How to Measure:**
The autocorrelation coefficient measures the extent of a linear relationship between time series values separated by a given lag. Tools include the autocorrelation function (ACF) and partial autocorrelation function (PACF).

#### Cointegration: Finding Assets That Walk Together

**The Core Concept:**
Cointegration is a statistical property that describes a long-run equilibrium relationship among two or more time series variables, even if the individual series are non-stationary. The variables may drift in the short run, but their linear combination is stationary.

**Plain English:**
Two stocks both wander randomly (non-stationary), but the spread between them is mean-reverting (stationary). This is the mathematical foundation of pairs trading.

**Formal Definition:**
Two series are cointegrated if they are both individually unit-root nonstationary (integrated of order I(1)) but there exists a linear combination that is unit-root stationary (integrated of order I(0)).

**Pairs Trading Application:**
A short-term disruption to an individual in the pair, such as a supply chain disruption solely affecting McDonald's, would lead to a temporary dislocation in their relative prices. A long-short trade carried out at this disruption point should become profitable as the two stocks return to their equilibrium value.

**Testing for Cointegration:**
The Engle-Granger procedure is the original test for cointegration. The idea is to first verify that the individual series are indeed non-stationary using the ADF test. Then regress one on the other using standard OLS and check if the residual series is stationary.

**Important Distinction:**
Although correlation and cointegration both describe some underlying relationship between variables, they are not synonymous. It is very possible for two time series to have weak/strong correlation but strong/weak cointegration.

Two stocks can move together daily (high correlation) but have a spread that never mean-reverts (no cointegration). Or they can have low correlation but their spread is perfectly stationary (strong cointegration). For pairs trading, cointegration matters far more than correlation.

---

### 1.4 Monte Carlo Simulation: Understanding Uncertainty

**Purpose:**
You can't know the future, but you can simulate thousands of possible futures to understand the range of outcomes your strategy might face.

**How It Works:**

1. Take your strategy's historical distribution of returns
2. Randomly resample from this distribution thousands of times
3. Generate thousands of potential equity curves
4. Analyze the distribution of outcomes

**What You Learn:**

- What's the probability your max drawdown exceeds 30%?
- What's the 5th percentile of 1-year returns?
- How often does your strategy experience 6 consecutive losing months?

**Critical Insight:**
Your backtest shows one path through history. Monte Carlo shows you 10,000 paths with the same return characteristics. If 20% of those paths blow up, you don't have a robust strategy—you have a lottery ticket that happened to win once.

---

## Part 2: Market Microstructure

### 2.1 Bid-Ask Spread: The Most Visible Transaction Cost

**Definition:**
The bid-ask spread is the difference between the highest price a buyer is willing to pay for an asset (bid price) and the lowest price at which a seller is willing to sell the same asset (ask price). In other words, it's the cost of entering or exiting a trade.

**Order Book Structure:**
The order book is divided into two sections: the bid side represents the demand for an asset (traders who want to buy), while the ask side represents the supply (traders who want to sell). The bid-ask spread represents the difference between the highest bid and the lowest ask.

**Example:**
You want to buy SPY:

- Best bid: $500.00 (someone wants to buy at this price)
- Best bid: $500.00 (someone wants to buy at this price)
- Best ask: $500.05 (someone wants to sell at this price)
- Spread: $0.05 (0.01% or 1 basis point)

You don't necessarily get the price we observe—you get the bid or the ask depending on the direction of trading. To ensure your trade can be filled, you will have to place a market order at the ask price of $500.05, even though the "market price" shown is $500.00.

**Liquidity Indicator:**
Bid-ask spreads reflect market liquidity and directly impact trading costs. Narrow spreads indicate higher liquidity and lower transaction costs, while wider spreads can make trades more expensive and harder to profit from, especially for short-term traders.

**What Determines the Spread:**
The spread may reflect: (1) order handling costs, (2) non-competitive pricing, (3) inventory risk that suppliers of immediacy must be compensated for, (4) the cost of granting a free trading option to informed traders, and (5) asymmetric information.

**Your Strategy Implication:**
If your mean reversion strategy on ETFs captures 5 basis points per trade on average, but the spread costs you 2 basis points round-trip, you've just lost 40% of your gross edge before commissions and slippage.

---

### 2.2 Market Impact: Why Your Backtest P&L Isn't Real

**Definition:**
Market impact is the effect that a market participant has when it buys or sells an asset. It is the extent to which the buying or selling moves the price against the buyer or seller—upward when buying and downward when selling.

**The Problem:**
Your backtest assumes you can buy 10,000 shares of a stock at the closing price. Reality: your order moves the price against you as you execute.

**Slippage Explained:**
Say you wanted to purchase 20,000 shares of SPY. The current ASK price of $151.08 only contains 3,900 shares being offered for sale. Using a market order to purchase your 20,000 shares would require buying at multiple price levels—the first 3,900 at $151.08, then more shares at higher prices like $151.09, $151.10, etc.

The average execution price becomes $151.11585 instead of $151.08. That $0.03585 difference across 20,000 shares is $717 in slippage costs.

**Common Market Impact Models:**

1. **Square Root Model (Kyle's Lambda):**
   Practitioners sometimes model market impact as proportional to the square root of traded volume, an approach that is supported by research.

2. **Almgren Model:**
   The Almgren model includes relative order size and volatility. It considers the fraction of outstanding shares traded daily, with higher volatility leading to higher impact costs.

3. **Temporary vs. Permanent Impact:**
   Temporary Impact captures the impact on transaction costs due to urgency or aggressiveness of the trade, while Permanent Impact estimates with respect to information or short-term alpha in a trade.

**Practical Example:**
Consider a mid-frequency statistical arbitrage portfolio with 100 million dollars in AUM at 2x leverage. At this level, we trade 20 billion dollars per year. Every single basis point (0.01%) of transaction cost translates into a 2% reduction of the algorithm's performance.

If your strategy generates 15% annual returns in backtest:

- 5 basis points in slippage = 10% real return
- 10 basis points in slippage = 5% real return
- 15 basis points in slippage = 0% real return (breakeven)

**The Heisenberg Uncertainty Principle of Finance:**
Market impact has often been described as the Heisenberg uncertainty principle of finance. Mathematically, the market impact cost of an order is the difference between the price trajectory of the stock with the order and the price trajectory that would have occurred had the order not been released to the market.

You can never know the "true" market impact because you can't simultaneously observe what would have happened without your trade.

**Critical Takeaway:**
Model slippage at 2-3x what you think it will be. If your backtest doesn't explicitly model realistic execution—meaning limit orders that might not fill, partial fills, walking the order book—you're building fantasy, not strategy.

---

### 2.3 Maker-Taker Fees: How Exchanges Actually Work

**The Basic Model:**
Maker-taker is an exchange pricing system. Its basic structure gives a transaction rebate to market makers providing liquidity (the makers) and charges a transaction fee to customers who take liquidity out of the market (the takers).

**Who Is Who:**

**Makers:**
When a trader submits a non-marketable limit order that rests in the order book, they are acting as a maker. Makers receive rebates for providing liquidity.

Example: Stock trading at $100. You place a limit order to buy at $99.95. Your order sits in the order book, adding liquidity. If it fills, you might receive a $0.002/share rebate.

**Takers:**
If another trader executes against this resting order with a market order or marketable limit order, they are the taker and pay fees for removing liquidity.

Example: You place a market order to buy at the best ask price of $100.05. You pay a fee, typically $0.003/share.

**Real-World Fee Structures:**

Equities:
The NYSE charges $0.0024 per share for aggressive marketable orders. However, this fee will be $0.00275 for nonfloor transactions and $0.0030 if you are a designated market maker. The schedule for maker rebates is more complex.

Crypto:
On Binance Futures, the highest tier of participants pay 0.02% for taker executions and receive 0.01% rebates for maker orders. Coinbase Advanced lists spot taker fees between 0.00%–0.60%, depending on tier.

**Why It Matters for Your Strategy:**

High-frequency strategies must optimize for maker rebates:
At the highest volume tiers, some exchanges pay rebates for providing liquidity instead of charging maker fees. According to Deribit Insights, maker rebates exist because exchanges profit from taker fees and spreads.

**Cost Comparison Example:**
Suppose a crypto exchange has a maker-taker fee model that charges 0.60% for takers and 0.40% for makers. If buying Ethereum at $4,500, a taker pays $27.00 in fees, while a maker placing a limit order pays $17.80—a $9.20 savings per trade.

Over 100 trades per month, that's $920 in additional costs if you always take liquidity instead of making it.

**The Routing Conflict:**
The broker-dealer may have an incentive to route to the venue with the highest rebate rather than diligently search out the venue likely to deliver the best execution of its customer's order. A similar conflict may exist for taker fees, as broker-dealers may seek to minimize their trading costs.

**Strategic Implications:**

1. Lower-frequency strategies (daily rebalancing): Maker fees don't matter much
2. Medium-frequency strategies (hourly): Optimize between maker rebates and execution certainty
3. High-frequency strategies: Maker rebates are often the primary edge

**Bottom Line:**
Transaction Cost Analysis (TCA) frameworks emphasize effective cost over nominal fees. Fees are one component in a multi-variable equation that includes spread, slippage, and opportunity cost.

---

## Part 3: Connecting It All - Transaction Costs as 50% of Edge Analysis

The roadmap states: "Transaction costs are 50% of your edge analysis. If you can't model them accurately, you're gambling."

Here's why this isn't hyperbole:

**Full Transaction Cost Breakdown (per round-trip trade):**

1. **Bid-Ask Spread**: 2-10 basis points (liquid ETFs: ~2 bps, less liquid stocks: ~10 bps)
2. **Commission**: 0-1 basis point (Interactive Brokers: ~$0.005/share on $100 stock = 0.5 bps)
3. **Market Impact/Slippage**: 2-20 basis points depending on:
   - Order size relative to average daily volume
   - Time of day (first/last 30 min has higher impact)
   - Volatility regime
4. **Maker-Taker Fees**: -2 to +3 basis points (can be positive or negative)

**Total**: Realistically 5-30 basis points per round-trip, depending on strategy frequency and liquidity.

**Strategy Profit Example:**

- Your mean reversion strategy captures 8 basis points per trade on average (gross)
- Transaction costs: 6 basis points per round-trip
- Net edge: 2 basis points per trade
- You've lost 75% of your edge to costs

**Annual Impact:**
If you trade 100 times per year with $100,000:

- Gross P&L: +$8,000 (8 bps × 100 trades × $100k)
- Transaction costs: -$6,000 (6 bps × 100 trades × $100k)
- Net P&L: +$2,000 (2% return)

Miss transaction costs in your backtest? You think you have a 8% strategy. You actually have a 2% strategy—and that's before accounting for regime changes, overfitting, and other risks.

**Why 50%:**
In most retail quant strategies with daily to weekly rebalancing:

- Transaction costs consume 30-60% of gross returns
- Risk management (position sizing, stops) consumes another 10-20%
- Actual alpha (your model's edge) is often only 30-50% of gross backtest returns

Model transaction costs wrong, and you've invalidated your entire research process.

---

## Resources for Deep Learning

**Statistics & Fat Tails:**

- "The Statistical Consequences of Fat Tails" by Nassim Nicholas Taleb
- Search: "fat tailed distributions finance" on Google Scholar for recent research

**Multiple Testing:**

- "Evidence-Based Technical Analysis" by David Aronson (Chapter on data mining)
- Search: "Bonferroni correction trading" for practical applications

**Time Series:**

- "Analysis of Financial Time Series" by Ruey S. Tsay
- statsmodels Python library documentation for practical implementation

**Market Microstructure:**

- "Trading and Exchanges" by Larry Harris (comprehensive textbook)
- "Market Microstructure in Practice" by Lehalle and Laruelle
- Interactive Brokers API documentation for order types

**Practical Implementation:**

- QuantStart.com tutorials on cointegration and backtesting
- Machine Learning for Trading by Stefan Jansen (GitHub resources)

---

## Practice Exercises

1. **Fat Tails**: Download SPY returns data. Calculate daily kurtosis over rolling 252-day windows. Plot kurtosis over time. When does it spike? What happened in markets?

2. **Multiple Testing**: Generate 100 random price series (white noise). Backtest a simple moving average crossover on each. How many show p < 0.05? Apply Bonferroni correction. How many survive?

3. **Cointegration**: Test pairs: (SPY, IVV), (XLE, XOP), (GLD, GDX). Which are cointegrated? Use the Engle-Granger test in Python's statsmodels.

4. **Transaction Costs**: Pick a strategy from a public GitHub repo. Add realistic bid-ask spread (0.02%), commission ($0.005/share), and slippage (0.03% per trade). How do returns change?

5. **Order Book**: Watch a liquid stock's Level 2 data for 10 minutes. Notice how the spread changes, how orders appear and disappear, how large orders impact prices. This is the reality your backtest must model.

---

## The Bottom Line

Phase 1 isn't about learning formulas. It's about internalizing that:

1. **Markets aren't normal** - extreme events happen far more than statistics textbooks suggest
2. **Statistical significance is a trap** - test enough variations and you'll find "significance" everywhere
3. **Stationarity matters** - most statistical tools assume it, markets don't have it
4. **Cointegration is real edge** - when you find it (rarely)
5. **Transaction costs kill** - they're often larger than your strategy's gross edge

Master these concepts before writing a single line of backtesting code. Otherwise, you're building an expensive random number generator.'
