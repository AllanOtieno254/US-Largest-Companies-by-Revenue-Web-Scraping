# -*- coding: utf-8 -*-
"""List_of_largest_companies_in_the_United_States_by_revenue

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mfBBBJfIbIPrEqLeGCecQZJww1r6z2ea

**SCRAPING DATA FROM A REAL WEBSITE + PANDAS**
"""

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find('table')

soup.find_all('table')[0]

soup.find_all('table', class_='wikitable sortable')

table = soup.find_all('table')[0]

print(table)

world_titles = table.find_all('th')
world_titles

world_table_titles = [title.text.strip() for title in world_titles]
world_table_titles

import pandas as pd
df = pd.DataFrame(columns = world_table_titles)
df

column_data = table.find_all('tr')

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  print(individual_row_data)
  length = len(df)
  df.loc[length] = individual_row_data ##we are checking the length of our dataframe each time is looping through
                                        ##then we gonna put the info in next location

df

df.to_csv(r'D:\ALLANS PROJECTS\webscraping\topcompanies.csv', index=False)