# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json

name_input = input("Enter a common animal name: ")

suggest = species.name_suggest(q=name_input, rank='SPECIES')

suggest_data = suggest['data']['results']

print(suggest_data)

data = suggest_data

for o in data:
    # print(o)
    key = o['key']
    occurs = occurrences.count(taxonKey=key)
    names = o['vernacularNames']
    if occurs > 0:
        for name in names:
            print(name['vernacularName'])
        print(key)
        print('Count: ' + str(occurs) + '\n')

# occurs = occurrences.search()

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
