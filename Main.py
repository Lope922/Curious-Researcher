# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json

suggest = species.name_suggest(q="white tiger", limit=50)

suggest_data = suggest['data']

print(suggest['data'])

data = suggest_data

for o in data:
    key = o['key']
    name = o['canonicalName']
    # print(key)
    # print(name)
    occurs = occurrences.count(taxonKey=key)
    print('Name: ' + name + '\nCount: ' + str(occurs))

# print(suggest['data'])

# print(suggest)
#
# number = occurrences.search(taxonKey=5959227, limit=250)
# occurs = number
#
# country_count = dict
#
#
#
# for o in occurs['results']:
#     country = o['country']
#
#     # Reads image of occurrence
#     # Could be used for the GUI images
#     # image = o['media']['identifier']
#
#     print(country)
#
# print(number)
