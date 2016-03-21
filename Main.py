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
    key = o['key']
    occurs = occurrences.count(taxonKey=key)
    if occurs > 0:
        print()
        try:
            canon_name = o['canonicalName']
        except:
            continue
        names = o['vernacularNames']
        descriptions = o['descriptions']
        try:
            print('Scientific name: ' + canon_name)
            print('Vernacular names: ')
            for name in names:
                # Used if all languages want to be included
                # print(name['vernacularName'])
                language = (name['language'])
                # Can be changed if user wants to select a specific language
                if language == 'eng':
                    print(name['vernacularName'])
            # print(wikipedia.search(canon_name))
            try:
                # pulls the wiki page based on canonical name in url (usually works)
                desc = wikipedia.page(canon_name, auto_suggest=True)
                # alternative wiki page including all sections
                page = wikipedia.WikipediaPage(canon_name)
                # pulls the summary page for the species
                summary = wikipedia.summary(canon_name, sentences=5)
                # experimental for section pages
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
        except:
            continue

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
