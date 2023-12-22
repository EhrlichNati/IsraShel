import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Table with no links inside
"""
url = 'https://www.rishonlezion.muni.il/Residents/SecurityEmergency/Pages/Publicshelter.aspx'

#Patch data
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

#Orgenize in table
data = []
for row in rows:
    cols = row.find_all(['td', 'th'])
    cols = [ele.get_text(strip=True) for ele in cols]
    data.append(cols)
df = pd.DataFrame(data)

# Specific modulations

df = pd.DataFrame(data).iloc[1:]
df = df.drop(columns=[5, 6])
df.rename(columns={0: "Shelter Num.", 1: 'Address', 2: 'Neighborhood', 3: 'Capacity', 4: 'Accessibility'}, inplace=True)

#Extract name
url_parts = url.split('.')
city_name = url_parts[1]

df.to_csv(f'/Users/netanelerlich/PycharmProjects/IsraShel/test_data/miklatim_{city_name}.csv', index=False)

"""

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








