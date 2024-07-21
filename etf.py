import click
import yfinance as yf
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from constants import ETF_EVAL_FUNCTIONS

load_dotenv()

@click.group()
def cli():
    """Main entry point for the CLI."""
    pass

@click.command()
@click.option('--tckr', help='The ticker symbol of the stock.')
def metrics(tckr):
    """
    Fetch and display key fundamental metrics.
    Expense ratio, net asset value, annualized return, dividend yield
    """
    etf = yf.Ticker(tckr)

    info = etf.info
    nav = info.get('navPrice', 'N/A')
    dividend_yield = info.get('yield', 0) * 100
    beta = info.get('beta3Year', 'N/A')

    yearlyReturn = info['ytdReturn'] * 100 if info.get('ytdReturn') else 'N/A'
    threeYearReturn = info['threeYearAverageReturn'] * 100 if info.get('threeYearAverageReturn') else 'N/A'
    fiveYearReturn = info['fiveYearAverageReturn'] * 100 if info.get('fiveYearAverageReturn') else 'N/A'

    click.echo(f'{tckr.upper()} key fundamental metrics:')
    click.echo('----------------------------------------------')

    click.echo(f'Net Asset Value: {nav}')
    click.echo(f'Dividend Yield: {dividend_yield}% ({ETF_EVAL_FUNCTIONS["Dividend Yield"](dividend_yield)})')
    if beta != 'N/A':
        click.echo(f'Beta: {beta} ({ETF_EVAL_FUNCTIONS["Beta"](beta)})')
    if yearlyReturn != 'N/A':
        click.echo(f'Yearly Return: {yearlyReturn}% ({ETF_EVAL_FUNCTIONS["Yearly Return"](yearlyReturn)})')
    if threeYearReturn != 'N/A':
        click.echo(f'3-Year Average Return: {threeYearReturn}% ({ETF_EVAL_FUNCTIONS["3-Year Average Return"](threeYearReturn)})')
    if fiveYearReturn != 'N/A':
        click.echo(f'5-Year Average Return: {fiveYearReturn}% ({ETF_EVAL_FUNCTIONS["5-Year Average Return"](fiveYearReturn)})')


# add to group
cli.add_command(metrics)

if __name__ == '__main__':
    cli()