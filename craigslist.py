from craigslist import CraigslistForSale

cl_s = CraigslistForSale(site='charlottesville', area='', category='moa',
                         filters={'query': 'iphone','min_price': 10, 'max_price': 80,'language': 'english'})

# You can get an approximate amount of results with the following call:
print(cl_s.get_results_approx_count())

for result in cl_s.get_results(sort_by='newest', geotagged=True):
    print(result)

# {
#     'id': u'4851150747',
#     'name': u'Near SFSU, UCSF and NEWLY FURNISHED - CLEAN, CONVENIENT and CLEAN!',
#     'url': u'http://sfbay.craigslist.org/sfc/roo/4851150747.html',
#     'datetime': u'2015-01-27 23:44',
#     'price': u'$1100',
#     'where': u'inner sunset / UCSF',
#     'has_image': False,
#     'has_map': True,
#     'geotag': (37.738473, -122.494721)
# }