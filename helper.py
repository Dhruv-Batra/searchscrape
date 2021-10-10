import pandas as pd
import numpy as np

def parseSearch(OgSearchTerm):
    return OgSearchTerm.replace(" ","+")

def exportData(items, df, n):
    try:
        item_title = items.find('h3', class_='s-item__title').text
    except Exception as e:
        item_title = 'None'

    df.loc[n, 'Title'] = item_title

    try:
        item_desc = items.find('div', class_='s-item__subtitle').text
    except Exception as e:
        item_desc = 'None'

    df.loc[n, 'description'] = item_desc

    try:
        item_price = items.find('span', class_='s-item__price').text
    except Exception as e:
        item_price = 'None'

    df.loc[n, 'Price'] = item_price

    try:
        item_shipping = items.find('span', class_='s-item__shipping s-item__logisticsCost').text
    except Exception as e:
        item_shipping = 'None'

    df.loc[n, 'Shipping'] = item_shipping

    try:
        item_top_seller = items.find('span', class_='s-item__etrs-text').text
    except Exception as e:
        item_top_seller = 'None'

    df.loc[n, 'Top Seller'] = item_top_seller

    try:
        item_stars = items.find('span', class_='clipped').text.split(' ')[0]
    except Exception as e:
        item_stars = 'None'

    df.loc[n, 'Stars'] = item_stars

    try:
        item_link = items.find('a', class_='s-item__link')['href']
    except Exception as e:
        item_link = 'None'

    df.loc[n, 'Link'] = item_link