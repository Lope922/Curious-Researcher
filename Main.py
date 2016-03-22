import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json
import wikipedia

def search_species(entry):

    # name_input = entry

    name_input = input("Enter a common species name: ")

    suggest = species.name_suggest(q=name_input, rank='SPECIES', limit=250)

    suggest_data = suggest['data']['results']

    print(suggest_data)

    data = suggest_data

    for o in data:
        key = o['key']
        occurs = occurrences.count(taxonKey=key)
        if occurs > 0:
            try:
                canon_name = o['canonicalName']
            except:
                continue
            names = o['vernacularNames']
            descriptions = o['descriptions']
            try:
                # If match found
                print('Scientific name: ' + canon_name)
                print('Vernacular names: ')
                match_found = False
                for name in names:
                    vern_name_match = name['vernacularName']
                    # Used if all languages want to be included
                    # print(name['vernacularName'])
                    language = (name['language'])
                    # Can be changed if user wants to select a specific language
                    if language == 'eng':
                        if name_input in vern_name_match and match_found == False:
                            match_found = True
                            print(vern_name_match)
                if match_found == False:
                    name_store = []
                    for name in names:
                        vern_name = name['vernacularName']
                        language = (name['language'])
                        if vern_name not in name_store:
                            name_store.append(vern_name)
                            if language == 'eng':
                                print(vern_name)

                # print(wikipedia.search(canon_name))
                try:
                    # pulls the wiki page based on canonical name in url (usually works)
                    desc = wikipedia.page(canon_name, auto_suggest=True)
                    # alternative wiki page including all sections
                    # page = wikipedia.WikipediaPage(canon_name)
                    # pulls the summary page for the species
                    summary = wikipedia.summary(canon_name, sentences=2)
                    # experimental for section pages
                    # sections = page.sections
                    # for section in sections:
                    #     print(section)
                    # github push error, delete this
                    print(summary)
                    # print(desc.content)
                except:
                    print("No description found")

                print('GBIF Key: ' + str(key))
                print('GBIF Species Page: ' + 'http://www.gbif.org/species/' + str(key))
                print('Count: ' + str(occurs) + '\n')
            except:
                continue



search_species('something')

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
