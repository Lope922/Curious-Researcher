# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json
import wikipedia


name_input = input("Enter a common animal name: ")

suggest = species.name_suggest(q=name_input, rank='SPECIES', limit=250)

suggest_data = suggest['data']['results']

print(suggest_data)

data = suggest_data

for o in data:
    # print(o)
    key = o['key']
    occurs = occurrences.count(taxonKey=key)
    canon_name = o['canonicalName']
    names = o['vernacularNames']
    descriptions = o['descriptions']
    if occurs > 0:
        print('Scientific name: ' + canon_name + '\n')
        print('Vernacular names: ')
        for name in names:
            # print(name['vernacularName'])
            language = (name['language'])
            if language == 'eng':
                print(name['vernacularName'])
        # print(wikipedia.search(canon_name))
        try:
            desc = wikipedia.page(canon_name, auto_suggest=True)
            page = wikipedia.WikipediaPage(canon_name)
            summary = wikipedia.summary(canon_name, sentences=5)
            # print('Short summary: ' + summary)
            # sections = page.sections
            # for section in sections:
            #     print(section)
            # github push error, delete this
            print(page.summary)
            # print(desc.content)
        except:
            print("No description found")

        print('GBIF Key: ' + str(key))
        print('GBIF Species Page: ' + 'http://www.gbif.org/species/' + str(key))
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
