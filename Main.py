from pygbif import species
from pygbif import occurrences
import wikipedia


def search_species(entry):
    # To be used when calling the method
    # name_input = entry

    # User input for testing purposes
    name_input = input("Enter a common species name: ")

    results = {}

    # Uses the pygbif method to find results
    suggest = species.name_suggest(q=name_input, rank='SPECIES', limit=25)

    # Pulls the results from the dataset in json format
    suggest_data = suggest['data']['results']

    # print(suggest_data)

    # Formats the data for pythonic purposes
    data = suggest_data

    # Reads data for each result
    for o in data:
        # Finds the gbif key
        key = o['key']
        # Uses pygbif to find number of occurrences of species key
        occurs = occurrences.count(taxonKey=key)
        # Searches occurrence data for the species key
        occur_search = occurrences.search(taxonKey=key)
        # print('occur search: ' + str(occur_search))

        # for country in countries:
        #     print(country)
        # print(occur_search)

        # Runs if species has occurred more than zero times
        if occurs > 0:
            try:
                # Tries to retrieve scientific name
                canon_name = o['canonicalName']
            except:
                continue
            # Vernacular name init
            vern_name = ''
            # Variable for list of vernacular names
            names = o['vernacularNames']
            # Summary init
            summary = ''
            try:
                # If match found
                print('Scientific name: ' + canon_name)
                print('Vernacular names: ')
                match_found = False
                # Reads from results in matched name
                for name in names:
                    # Variable for vernacular name
                    vern_name = name['vernacularName']
                    # Used if all languages want to be included
                    # print(name['vernacularName'])
                    language = (name['language'])
                    # Can be changed if user wants to select a specific language
                    if language == 'eng':
                        # Checks if vernacular name is matched with search input
                        if name_input in vern_name and match_found is False:
                            match_found = True
                            print(vern_name)
                # If no exact match is found it reads the first vernacular name
                if match_found is False:
                    name_store = []
                    for name in names:
                        vern_name = name['vernacularName']
                        language = (name['language'])
                        if vern_name not in name_store:
                            name_store.append(vern_name)
                            if language == 'eng':
                                print(vern_name)
                # Adds scientific and vernacular name to results dictionary
                results.setdefault(canon_name, []).append(vern_name)

                # print(wikipedia.search(canon_name))
                try:
                    # pulls the wiki page based on canonical name in url (usually works)
                    # desc = wikipedia.page(canon_name, auto_suggest=True)
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
                    results.setdefault(canon_name, []).append(summary)
                    # print(desc.content)
                except:
                    print("No description found")

                print('GBIF Key: ' + str(key))
                print('GBIF Species Page: ' + 'http://www.gbif.org/species/' + str(key))
                print('Count: ' + str(occurs))

                # This reads results for occurences and finds countries the species
                # was observed in and how many occurrences there
                occur_data = occur_search['results']
                countries = {}
                for occur in occur_data:
                    try:
                        country = occur['country']
                        if country not in countries:
                            countries[country] = 1
                        else:
                            countries[country] += 1
                            # print(occur['country'])
                    except:
                        continue
                # for country in countries:
                #     print(country)
                sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
                if countries != {}:
                    print('Top 3 Countries Observed: ')
                    for country in sorted_countries[:3]:
                        print(str(country))
                print('\n')

                # return canon_name, vern_name, summary
            except:
                continue

    print(results)

    # To be used when calling the method
    # return results

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
