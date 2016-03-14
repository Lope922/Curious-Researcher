# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json

# suggest = species.name_suggest(q="blue whale")
#
# print(suggest)

number = occurrences.search(taxonKey=5959227, limit=250)

occurs = number

for o in occurs['results']:
    country = o['country']
    print(country)

print(number)
