from craigslist import CraigslistForSale

cl_s = CraigslistForSale(site='charlottesville', area='', category='',
                         filters={'query': 'iphone 11','min_price': 50, 'max_price': 1000,'language': 'english'})

# You can get an approximate amount of results with the following call:
print(cl_s.get_results_approx_count())

for result in cl_s.get_results(sort_by='newest', geotagged=True):
    print(result['name'])