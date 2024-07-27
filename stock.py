import click
import yfinance as yf
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from utils import get_stock_data, get_industry_averages, get_discount_rate, get_growth_rate, get_free_cash_flow \
    , estimate_terminal_growth_rate, get_dividend_growth_rate
from constants import STOCK_EVAL_FUNCTIONS

load_dotenv()

@click.group()
def cli():
    """Main entry point for the CLI."""
    pass

@click.command()
@click.option('--tckr', help='The ticker symbol of the stock.')
def income(tckr):
    """
    Fetch and display company net income for its entire history.
    """
    click.echo(f'{tckr.upper()} net income for the entire history:')
    click.echo('----------------------------------------------')
    
    params = {
        "function": "INCOME_STATEMENT",
        "symbol": tckr,
        "apikey": os.getenv('ALPHA_VANTAGE_API_KEY')
    }
    data = requests.get("https://www.alphavantage.co/query", params=params).json()

    if "annualReports" in data:

        net_income_data = {
            report["fiscalDateEnding"]: float(report["netIncome"]) for report in data["annualReports"]
        }

        years = list(net_income_data.keys())[::-1]
        incomes = list(net_income_data.values())[::-1]

        for year, income in zip(years, incomes):
            click.echo(f'{year}: {income}')

        plt.figure(figsize=(10, 5))
        plt.plot(years, incomes, marker='o')
        plt.xlabel('Years')
        plt.ylabel('Net Income (USD)')
        plt.title(f'{tckr.upper()} Net Income Chart')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: "{:,}".format(int(x))))
        plt.tight_layout()
        plt.show()
    
    else:
        click.echo('Net Income data is not available for this stock.')

@click.command()
@click.option('--tckr', help='The ticker symbol of the stock.')
def metrics(tckr):
    """
    Fetch and display key fundamental metrics along with industry benchmark.
    """
    metrics = get_stock_data(tckr)
    sector = yf.Ticker(tckr).info.get('sector')
    benchmark_metrics = get_industry_averages(sector)
    click.echo(f'{tckr.upper()} key fundamental metrics:')
    click.echo('----------------------------------------------')

    for key, value in metrics.items():
        if value is None:
            continue

        perf = STOCK_EVAL_FUNCTIONS[key](value, benchmark_metrics[key])
        click.echo(f'{key}: {value} (Industry Avg: {benchmark_metrics[key]}) - {perf}')

@click.command
@click.option('--tckr', help='The ticker symbol of the stock.')
def summary(tckr):
    """
    Fetch and display summary of company.
    """
    summary = yf.Ticker(tckr).info
    click.echo(f'{tckr.upper()} summary:')
    click.echo('----------------------------------------------')
    click.echo(f'Description: {summary.get("longBusinessSummary")}')

@click.command()
@click.option('--tckr', help='The ticker symbol of the stock.')
def dcf(tckr):
    """
    Calculate intrinsic value for a stock based on dcf analysis.
    """
    growth_rate = get_growth_rate(tckr)/100
    discount_rate = get_discount_rate(tckr)/100
    free_cash_flow = get_free_cash_flow(tckr)
    terminal_growth_rate = estimate_terminal_growth_rate(growth_rate)
    years = 10
    
    click.echo(f'Growth rate: {growth_rate}')
    click.echo(f'Discount rate: {discount_rate}')
    click.echo(f'Free cash flow: {free_cash_flow}')
    click.echo(f'Terminal growth rate: {terminal_growth_rate}')

    cash_flows = []
    discounted_cash_flows = []

    for year in range(1, years + 1):
        next_cash_flow = free_cash_flow * ((1 + growth_rate) ** year)
        cash_flows.append(next_cash_flow)
    
    for year in range(1, years + 1):
        discounted_cash_flow = cash_flows[year - 1] / ((1 + discount_rate) ** year)
        discounted_cash_flows.append(discounted_cash_flow)
    
    terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)

    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

    intrinsic_value = sum(discounted_cash_flows) + discounted_terminal_value
    
    click.echo(f'Intrinsic value of {tckr} is: ${intrinsic_value:.2f} billion')
    number_of_shares = yf.Ticker(tckr).info['sharesOutstanding']
    click.echo(f'Number of shares: {number_of_shares}')
    click.echo(f'Intrinsic value per share: ${intrinsic_value / number_of_shares:.2f}')
    click.echo(f'Current price: ${yf.Ticker(tckr).info["currentPrice"]}')

@click.command()
@click.option('--tckr', help='The ticker symbol of the stock.')
def ddm(tckr):
    """
    Calculate intrinsic value for a stock based on dividend discount model.
    """
    # Fetch stock data
    stock = yf.Ticker(tckr)
    
    # Retrieve dividend data
    info = stock.info
    dividend_yield = info.get('dividendYield', None)
    if dividend_yield is None:
        raise ValueError("This stock does not pay dividends.")

    click.echo(f'Dividend yield: {dividend_yield}')
    current_price = info.get('currentPrice', None)
    if current_price is None:
        raise ValueError("Current stock price data is not available for this stock.")
    dividend = dividend_yield * current_price

    discount_rate = get_discount_rate(tckr)/100
    stock_price = dividend / (discount_rate - get_dividend_growth_rate(tckr)/100)

    click.echo(f'Intrinsic value of {tckr} is: ${stock_price:.2f}')
    click.echo(f'Current price: ${current_price}')
    return stock_price
    

# add to group
cli.add_command(income)
cli.add_command(metrics)
cli.add_command(summary)
cli.add_command(dcf)
cli.add_command(ddm)

if __name__ == '__main__':
    cli()