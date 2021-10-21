import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from helper import parseSearch, exportData
from datetime import datetime

# input parameters and parse to transform into acceptable input
OgSearchTerm = "iphone 6"
searchTerm = parseSearch(OgSearchTerm)
minPrice = "50"
maxPrice = "80"

ebay_url = 'https://www.ebay.com/sch/%s&_udlo=%s&_udhi=%s&_sop=15'%(searchTerm, minPrice, maxPrice)
response = requests.get(ebay_url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")

df = pd.DataFrame(columns = ['Title', 'Price','description', 'Shipping' , 'Top Seller','Stars', 'Link'])

n=0

for items in soup.find_all('li', class_='s-item'):
    exportData(items, df, n)
    n+=1

print(df.head())

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%H_%M_%S=%d_%m_%Y")

# CHANGE ME TO THE FILEPATH TO YOUR RESULTS DIRECTORY
filepath="C:/Users/dhruv/Documents/searchscrape/Results/"

# add search term and datetime to filename to create unique, descriptive filename
filepath+=str(OgSearchTerm+'='+dt_string+'.xlsx')

# create excel file
df.to_excel(filepath, index = False)
