import requests
from bs4 import BeautifulSoup
import pandas as pd

def eth_top_holders_scraper():

    url = 'https://etherscan.io/accounts'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    addresses = []
    name_tags = []

    table = soup.find('table')

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')

        address_link = cols[1].find('a')
        if address_link and 'href' in address_link.attrs:
            href = address_link['href']
            full_address = href.split('/')[-1].lower()
            addresses.append(full_address)

        name_tags.append(cols[2].text.strip())

    df = pd.DataFrame({
        'address': addresses,
        'name_tag': name_tags   
    })

    return df