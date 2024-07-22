import click
import yfinance as yf
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from utils import get_stock_data, get_industry_averages, get_discount_rate, get_growth_rate, get_free_cash_flow \
    , estimate_terminal_growth_rate
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
def value(tckr):
    """
    Calculate intrinsic value for a stock based on dcf analysis.
    """
    def calculate_present_value_of_cash_flows(free_cash_flow, growth_rate, discount_rate, years):
        present_value = 0
        for year in range(1, years + 1):
            cash_flow = free_cash_flow * (1 + growth_rate) ** year
            present_value += cash_flow / (1 + discount_rate) ** year
        return present_value

    def calculate_terminal_value(free_cash_flow, growth_rate, discount_rate):
        terminal_value = free_cash_flow * (1 + growth_rate) / (discount_rate - growth_rate)
        return terminal_value

    growth_rate = get_growth_rate(tckr)/100
    discount_rate = get_discount_rate(tckr)/100
    free_cash_flow = get_free_cash_flow(tckr)
    terminal_growth_rate = estimate_terminal_growth_rate()
    years = 10
    
    # Calculate present value of cash flows for the first 10 years
    present_value_of_cash_flows = calculate_present_value_of_cash_flows(free_cash_flow, growth_rate, discount_rate, years)
    
    # Calculate terminal value and present value of the terminal value
    terminal_value = calculate_terminal_value(free_cash_flow * (1 + growth_rate) ** years, terminal_growth_rate, discount_rate)
    present_value_of_terminal_value = terminal_value / (1 + discount_rate) ** years

    # Total intrinsic value
    intrinsic_value = present_value_of_cash_flows + present_value_of_terminal_value

    click.echo(f'Intrinsic value of {tckr} is: ${intrinsic_value:.2f} billion')
    number_of_shares = yf.Ticker(tckr).info['sharesOutstanding']
    click.echo(f'Intrinsic value per share: ${intrinsic_value / number_of_shares:.2f}')

# add to group
cli.add_command(income)
cli.add_command(metrics)
cli.add_command(summary)
cli.add_command(value)

if __name__ == '__main__':
    cli()