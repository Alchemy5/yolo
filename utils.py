import os
import json
from constants import STOCKS
import yfinance as yf

def get_stock_data(ticker):
    """
    Given a tckr return key fundamental metrics.
    """
    stock = yf.Ticker(ticker)
    
    # Fetch financial data
    info = stock.info
    metrics = {
        'P/E Ratio': info.get('trailingPE', None),
        'PEG Ratio': info.get('pegRatio', None),
        'Net Profit Margin': info.get('profitMargins') * 100 if info.get('profitMargins') else None,
        'ROE': (info.get('returnOnEquity') * 100) if info.get('returnOnEquity') else None,
        'ROA': (info.get('returnOnAssets') * 100) if info.get('returnOnAssets') else None,
        'Debt to Equity Ratio': info.get('debtToEquity'),
        'Current Ratio': info.get('currentRatio'),
        'Quick Ratio': info.get('quickRatio'),
        'Dividend Yield': round(info.get('dividendYield') * 100, 2) if info.get('dividendYield') else None,
        'EPS': info.get('trailingEps')
    }

    return metrics

def get_industry_averages(sector):
    """
    Fetch and return industry averages for key fundamental metrics.
    """
    if os.path.exists(f'output/cache/{sector}.json'):
        with open(f'output/cache/{sector}.json', 'r') as f:
            return json.load(f)
    
    if not os.path.exists('output/cache'):
        os.makedirs('output/cache')
    
    if sector not in STOCKS:
        raise Exception("Stocks in this sector not supported yet!")

    sector_stocks = STOCKS[sector]
    metrics_sum = {}
    count = 0

    try:
        for stock in sector_stocks:
            metrics = get_stock_data(stock)

            if any(value is None for key, value in metrics.items() if key != 'Dividend Yield'):
                print(f"Skipping {stock} due to missing data")
                continue

            for key, value in metrics.items():
                if value is not None:
                    metrics_sum[key] = metrics_sum.get(key, 0) + value

            count += 1
            print(f"Processed {stock}")
    except Exception as e:
        print(e)
        import pdb; pdb.set_trace()

    metrics_avg = {key: value / count for key, value in metrics_sum.items()}

    with open(f'output/cache/{sector}.json', 'w') as f:
        json.dump(metrics_avg, f)
    
    return metrics_avg