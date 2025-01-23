import json

TICKERS = {
    "tech": ["AAPL", "MSFT", "GOOGL", "META", "NVDA", "INTC", "AMD", "TSM", "CSCO", "ORCL"],
    "finance": ["JPM", "BAC", "GS", "MS", "C", "WFC", "BLK", "SCHW", "AXP", "V"],
    "healthcare": ["JNJ", "PFE", "MRK", "UNH", "ABBV", "TMO", "DHR", "BMY", "LLY", "AMGN"],
    "retail": ["AMZN", "WMT", "COST", "HD", "TGT", "LOW", "EBAY", "DG", "DLTR", "KR"],
    "energy": ["XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO", "OXY", "PXD"]
}

TRADERS = {
    "execution": [f"trader{i}" for i in range(1, 11)],
    "portfolio": [f"pm{i}" for i in range(1, 6)],
    "analyst": [f"analyst{i}" for i in range(1, 8)],
    "algo": [f"algo_trader{i}" for i in range(1, 5)],
    "market_maker": [f"mm{i}" for i in range(1, 4)]
}

ORDER_FLOW = {
    "sweep": {
        "desc": "Multiple exchange sweep",
        "prob": 0.2,
        "min_size": 5000,
        "exchanges": ["NYSE", "NASDAQ", "IEX", "BATS", "ARCA"]
    },
    "iceberg": {
        "desc": "Hidden liquidity",
        "prob": 0.15,
        "min_size": 10000,
        "exchanges": ["NYSE", "NASDAQ", "IEX"]
    },
    "peg": {
        "desc": "Pegged to VWAP",
        "prob": 0.3,
        "min_size": 1000,
        "exchanges": ["NYSE", "NASDAQ", "ARCA"]
    },
    "dark": {
        "desc": "Dark pool execution",
        "prob": 0.25,
        "min_size": 15000,
        "exchanges": ["MS_POOL", "UBS_MTF", "JPM_POOL", "GS_SIGMA"]
    },
    "block": {
        "desc": "Large block trade",
        "prob": 0.1,
        "min_size": 50000,
        "exchanges": ["NYSE", "NASDAQ"]
    },
    "twap": {
        "desc": "Time-weighted execution",
        "prob": 0.2,
        "min_size": 2000,
        "exchanges": ["NYSE", "NASDAQ", "IEX"]
    },
    "close": {
        "desc": "Market on close",
        "prob": 0.1,
        "min_size": 5000,
        "exchanges": ["NYSE", "NASDAQ"]
    }
}

# Load config
def get_config():
    return {
        "tickers": TICKERS,
        "traders": TRADERS,
        "order_flow": ORDER_FLOW
    }