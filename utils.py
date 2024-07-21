import os
import json

def get_industry_averages(sector):
    """
    Fetch and return industry averages for key fundamental metrics.
    """
    if os.exists(f'output/cache/{sector}.json'):
        with open(f'output/cache/{sector}.json', 'r') as f:
            return json.load(f)
    if not os.exists('output/cache'):
        os.makedirs('output/cache')
    