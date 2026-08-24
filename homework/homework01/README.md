# The 52-Week High Effect in Equity Returns
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Investors often assume stocks near a 52-week high are "overbought" and due for a pullback, but a well-documented study by George & Hwang (2004) suggests the opposite. Stocks near their highs tend to keep outperforming over the following weeks (the "52-week high effect"). This project tests whether that pattern holds in a recent, small sample of liquid stocks. Does proximity to the 52-week high predict subsequent returns better than a naive baseline?

## Stakeholder & User
The primary stakeholder is a junior analyst on an equity research or quant desk who needs to evaluate whether a known market anomaly still holds in current data before it's considered for further research. The end user is a  portfolio manager who decides whether the pattern is worth deeper investigation or ignored as noise.

## Useful Answer & Decision
This project uses descriptive/predictive research, because it is testing whether a documented pattern replicates, not why it exists. The metrics used are the regression coefficient and R² of forward returns on "distance from 52-week high". There is also a classification accuracy (up/down) vs. a naive baseline. The result will show whether the effect held, how strong it was, and whether it warrants further research.

## Assumptions & Constraints
* The data is daily price history via yfinance for 15-20 liquid, large-cap stocks. Data acquisition is free with no latency/licensing issues.

* The analysis window is 3 years of daily data, enough to compute rolling 52-week highs and forward returns without overfitting.

* There are no transaction costs, slippage, or portfolio construction, since it is a signal/replication study, not a backtest.

## Known Unknowns / Risks
* The effect may be weaker or absent in the chosen sample/period. A null result is still a valid, reportable finding, especially since this study uses a far smaller and more recent sample than the original research, so a null result here wouldn't contradict the literature.

* Recent work (Barroso and Wang, 2021) finds the original 52-week high effect is largely limited to small-cap stocks and may just reflect ordinary price momentum rather than a distinct effect, so results will be checked against plain momentum as a robustness test.

* There is survivorship bias because only currently-liquid, currently-listed stocks are included, which could inflate apparent effect strength.

* The forward-return windows chosen (e.g., 5-day, 20-day) are somewhat arbitrary and results may be sensitive to that choice. More than one window will be tested to check robustness.

* No control for sector or market-wide moves, so some of the "effect" could reflect broader momentum rather than the 52-week-high signal specifically.

## Lifecycle Mapping
- Define a testable version of the 52-week high effect → Problem Framing & Scoping (Stage 01) → This README + stakeholder memo
- 
- Pull price data via API → Data Acquisition/Ingestion (Stage 04) → Raw data files in data/raw/
  
- Store cleaned, joined dataset → Data Storage (Stage 05) → data/processed/merged_dataset.csv
  
- Handle missing values, align trading days → Data Preprocessing (Stage 06) → Cleaning notebook section
  
- Check for outlier return days → Outlier Analysis (Stage 07) → EDA notebook section
  
- Visualize distance-from-high vs. forward return → Exploratory Data Analysis (Stage 08) → Charts in notebook + slide deck
  
- Construct "distance from 52-week high" feature, multiple forward-return windows → Feature Engineering (Stage 09) → Feature table in notebook
  
- Fit linear regression (magnitude) and logistic regression (direction) → Modeling (Stage 10) → Model outputs in notebook
  
- Evaluate against naive baseline, test robustness across windows → Evaluation & Risk Communication (Stage 11) → Metrics table + Assumptions & Risks section
  
- Communicate findings to research desk persona → Results Reporting & Stakeholder Communication (Stage 12) → Slide deck + stakeholder memo

## Repo Plan
The repo is organized into four folders: data/ holds raw API pulls and the cleaned/merged dataset, src/ holds reusable Python functions for data pulling, cleaning, and modeling, notebooks/ holds the main analysis notebook with markdown documentation, and docs/ holds the stakeholder memo and slide deck export. Commits happen after each lifecycle stage is completed including data pull, cleaning, EDA, modeling, and reporting, rather than as one large end-of-project commit. So the commit history reflects the pipeline.
