import requests
from bs4 import BeautifulSoup

def get_county_spending_data():
    url = 'https://example-auditor-general-website.com/county-spending'
    response = requests.get(url)
    
    if response.status_code == 200:
       
        return [
            {'county': 'County A', 'date': '2024-01-01', 'amount': 100000, 'description': 'Description A'},
            {'county': 'County B', 'date': '2024-01-02', 'amount': 150000, 'description': 'Description B'},
        ]
    else:
        return None
