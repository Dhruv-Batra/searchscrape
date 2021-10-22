import requests
from bs4 import BeautifulSoup
import pandas as pd
from helper import parseSearch, exportData, exportCraig
from datetime import datetime
from craigslist import CraigslistForSale

# input parameters and parse to transform into acceptable input
OgSearchTerm = "iphone 11"
searchTerm = parseSearch(OgSearchTerm)
minPrice = "50"
maxPrice = "1000"

# Ebay web scrape for product
ebay_url = 'https://www.ebay.com/sch/%s&_udlo=%s&_udhi=%s&_sop=15'%(searchTerm, minPrice, maxPrice)
response = requests.get(ebay_url)
print(response)
soup = BeautifulSoup(response.text, "html.parser")

# initialize dataframe
df = pd.DataFrame(columns = ['Title', 'Price','description', 'Shipping' , 'Top Seller','Stars', 'Link'])

# populate dataframe with ebay listings
n=0
for items in soup.find_all('li', class_='s-item'):
    exportData(items, df, n)
    n+=1

# craigslist web scrape for product
cl_s = CraigslistForSale(site='charlottesville', area='', category='',
                         filters={'query': OgSearchTerm,'min_price': minPrice, 'max_price': maxPrice,'language': 'english'})
print("Craigslist Results "+str(cl_s.get_results_approx_count()))

#populate data frame with craigslist results
for result in cl_s.get_results(sort_by='newest', geotagged=True):
    exportCraig(result,df,n)
    n+=1

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%H_%M_%S=%d_%m_%Y")

# CHANGE ME TO THE FILEPATH TO YOUR RESULTS DIRECTORY
filepath="C:/Users/dhruv/Documents/searchscrape/Results/"

# add search term and datetime to filename to create unique, descriptive filename
filepath+=str(OgSearchTerm+'='+dt_string+'.xlsx')

# sort data frame by price, clean data, and create excel file
df.sort_values(by='Price',ascending=True, inplace=True)
df = df[df.Price != float(9999999)]
df.to_excel(filepath, index=False)

