import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape (Auditor General's county spending page)
url = 'https://example-auditor-general-website.com/county-spending'

def scrape_county_spending():
    # Send an HTTP GET request to fetch the page content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing spending data
        table = soup.find('table', {'id': 'county_spending_table'})
        
        # Create a CSV file to store the scraped data
        with open('county_spending_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['County', 'Spending', 'Year'])

            for row in table.find_all('tr')[1:]:  # Skip header row
                columns = row.find_all('td')
                county = columns[0].text.strip()
                spending = columns[1].text.strip()
                year = columns[2].text.strip()

                writer.writerow([county, spending, year])

        print("Data scraped and saved to county_spending_data.csv")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Call the function to run the scraper
if __name__ == "__main__":
    scrape_county_spending()
