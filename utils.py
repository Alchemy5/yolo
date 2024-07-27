import os
import json
from constants import STOCKS
import yfinance as yf
import numpy as np
from lxml import html
import requests
from dotenv import load_dotenv

load_dotenv()

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
        'Debt to Equity Ratio': info.get('debtToEquity')/100 if info.get('debtToEquity') else None,
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

def get_growth_rate(tckr):
    """
    Given ticker calculate average growth rate in revenue.
    """
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={tckr}&apikey={os.getenv("ALPHA_VANTAGE_API_KEY")}'
    
    data = requests.get(url).json()
    revenues = {}
    annual_reports = data.get('annualReports', [])
    for report in annual_reports:
        fiscal_date_ending = report.get('fiscalDateEnding')
        total_revenue = report.get('totalRevenue')
        revenues[fiscal_date_ending] = int(total_revenue)
    
    revenues = list(revenues.values())[::-1]
    revenues = revenues[len(revenues)-10:] # past 10 years
    growth_rates = []
    
    for i in range(1, len(revenues)):
        growth_rate = ((revenues[i] / revenues[i-1]) - 1) * 100
        growth_rates.append(growth_rate)
    
    return sum(growth_rates) / len(growth_rates)

def get_discount_rate(tckr):
    """
    WACC calculation.
    """
    stock = yf.Ticker(tckr)
    beta = stock.info.get('beta', None)
    equity_value = stock.info.get('marketCap', None)

    balance_sheet = stock.balance_sheet
    long_term_debt = balance_sheet.loc['Long Term Debt'].iloc[0]
    debt_value = long_term_debt

    if not beta:
        raise Exception('Beta not available for this stock.')

    risk_free_rate = 4.242/100
    market_risk_premium = 5/100
    cost_of_debt = 4/100

    cost_of_equity = risk_free_rate + beta * market_risk_premium

    total_value = equity_value + debt_value
    weight_equity = equity_value / total_value
    weight_debt = debt_value / total_value

    wacc = (weight_equity * cost_of_equity) + (weight_debt * cost_of_debt * (1 - 21/100)) # corporate tax rate is 21%

    return wacc * 100  # Convert back to percentage

def get_free_cash_flow(ticker):
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow
    if 'Free Cash Flow' in cash_flow.index:
        free_cash_flow = cash_flow.loc['Free Cash Flow'].iloc[0]
        return free_cash_flow
    else:
        raise Exception('Free Cash Flow data not available for this stock.')
    
def estimate_terminal_growth_rate(growth_rate):
    """
    """
    # A conservative approach might use a rate close to the economic growth rate or slightly below it.
    return growth_rate / 2