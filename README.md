# Homework 0

## Required work

1. Please add your name and GitHub username to the list below. (Due to student privacy laws, I can't actually require you to post your name in a public repository. If you have privacy concerns, you can email me for an alternate way to complete the assignment.)

2. Edit the file `names.py` to define a function which returns your name WITHOUT using any string literals that contain any letters of your name, then add your function to the list `NAME_FUNCTIONS`, so that when the program runs, it prints the names of everyone who completed the assignment. I provided an example to get you started. I did it in a somewhat overly-mathematical way, but you're welcome to do it in a simpler way. The point of this assignment is to make sure everyone can use GitHub, not to test your math skills.

Note: Since I don't have your GitHub usernames yet, I can't add you as collaborators, so you won't be able to edit my files. You can make your own fork and submit a pull request. After that, I can add you as a collaborator so you can make further changes without waiting for my approval, if you want.

This assignment is due by the end of the day on Friday, September 5.

## GitHub Usernames

Add yourself to the list below. (Please keep the list alphabetized by last name.)

Jianping Chen: alanchen8647
James Sundstrom: JamesSundstrom
Hasib Shaif: hasibshaif
Anis Tarafdar: anistarafdar
Gregory Tomchuk: gtomchuk2005
Samuel Hanono: SamuelHanono


## Idea Box

Edit below for any idea you're looking to work on with classmates with your name next to it. Feel free to be as broad or descriptive for your idea for now. Listed below are just suggestions of ideas

- Video Game (Anis is interested in this!)
    - Unreal Engine project?
    - game engine from scratch?
- Machine Learning
    - fafake news detector ?
    - facial recognition?
    - image upscaling?
- Web App
    - light weight messaging client
    - ???
- Market Micro-Alpha — ML-guided Pairs Trading (Samuel Hanono)
    Goal: Predict mean-reversion of price spreads; small, fun, interpretable.
    Data: Daily OHLCV (2015–2024) for ~30–50 US stocks/ETFs via yfinance.
    Features: Spread z-score, rolling β, residuals, half-life, RSI(spread), vol.
    Pair pick: Engle–Granger/Johansen cointegration tests.
    Labels: Revert ≥ X% within 5 trading days (1/0).
    Models: Logistic (baseline); Gradient Boosting / Random Forest.
    Signal: Enter |z| ≥ 2 & model-prob > τ; exit at mean or T+5; size by ATR; costs 2–5 bps.
    Backtest: Walk-forward by year; ≤5 concurrent pairs; position limits.
    Metrics: CAGR, Sharpe, max DD, hit-rate, turnover; SHAP for explainability.
    Deliverables: One clean notebook + backtest.py; 1-page PDF with equity curve.
    Stretch: 15-min intraday ETFs; improved cost model; Streamlit dashboard.

