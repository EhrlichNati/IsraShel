import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL to scrape
url = 'https://he.wikipedia.org/wiki/ערים_בישראל'


# Extract the part of the URL after 'www.'
url_parts = url.split('/')
domain_name = url_parts[2].split('.')[1]  # Gets the part after 'www.'

# Create a directory name
directory_name = f'{domain_name} ({url})'
directory_path = os.path.join('/Users/netanelerlich/PycharmProjects/IsraShel/test_data', directory_name)

# Create the directory if it does not exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Fetch data
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables
tables = soup.find_all('table')

# Process each table
for num_table, table in enumerate(tables):
    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.get_text(strip=True) for ele in cols]
        table_data.append(cols)
    df = pd.DataFrame(table_data)

    # Define file path
    file_name = f'{domain_name}_{num_table}.csv'
    file_path = os.path.join(directory_path, file_name)

    # Save to CSV
    df.to_csv(file_path, index=False)

# With links inside the table
"""
# URL of the webpage containing the table
url = 'https://www.ashkelon.muni.il/service/emergency/Pages/RECEIVERS.aspx?SortField=Title&SortDir=Asc&View=%7bC5898028%2dBBA8%2d49D7%2dAFC2%2d2D391004FDD8%7d'

# Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table', class_='ms-listviewtable')  # Adjust class as needed

# Extract rows
rows = table.find_all('tr')

# Organize in table
data = []
for row in rows:
    cols = row.find_all('td')  # Assuming you want to skip header rows
    row_data = []
    for ele in cols:
        # Check if cell contains a link
        link = ele.find('a')
        if link:
            # Extract text from link
            text = link.get_text(strip=True)
        else:
            # Extract text directly from cell
            text = ele.get_text(strip=True)
        row_data.append(text)
    data.append(row_data)

df = pd.DataFrame(data).iloc[1:]
df.rename(columns={0: "Address", 1: 'Neighborhood', 2: 'Additional Guidance'}, inplace=True)

#Extract name
url_parts = url.split('.')
city_name = url_parts[1]

df.to_csv(f'/Users/netanelerlich/PycharmProjects/IsraShel/test_data/miklatim_{city_name}.csv', index=False)
"""


