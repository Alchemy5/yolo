import click
import yfinance as yf
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import requests
import pandas as pd

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
def key_metrics(tckr):
    """
    Fetch and display key fundamental metrics along with industry benchmark.
    """


# add to group
cli.add_command(income)

if __name__ == '__main__':
    cli()