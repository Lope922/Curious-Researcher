import requests
import json
import os

unique_keys = []
scientific_names = []
description = []
# each animal will now have to have one name entered by the user 
# and a scientific name
# as well as a description

class Animal():

    def __init__(self, name, sciName, Description):
        self.Name = name
        self.SciName = sciName
        self.Desc = Description
        # self.UniqueKey = uniqueKey
        return self

	# this method needs the response passed in from GBIF to extract a scientific name
	
    def extraction(self, data):

        for item in data['results']:
            # this is the unique keys list that will be used to retrieve the other descriptions and infomation.
           # print("Here is the family " + str(item['family']))
           # unique_keys.append(item['key'])
           # print("Here is that animals key " + str(item['key']))
            print("Here is the scientific name " + str(item['scientificName']))
            scientific_names.append(item['scientificName'])
            description.append(item['descriptions'])

    # try and make a request with the unique key and extract information
            # todo store the name to display as a value. and move onto displaying image in web page on web server. Either flask or Django

            #TODO also look up how to obtain a breif description and store it somehow if it is in english.


        #   #todo get this to work for each key
        #     print("here is the description " + str(item['descriptions']))
        # for animals in data['key']:
        #     print(data[str(unique_keys)])
        # todo use the species key to access each individual description
      # for item in unique_keys:
        #     print(str(item))

    # this method needs to search the term that is passed into it. and it should be passed in through the button click from the web page

    # this method returns the json data to be processed in python
def search(keyword):
    # Limit the results to 5
    the_url = "http://api.gbif.org/v1/species/search?q={0}&rank=GENUS&limit=5&language=en".format(str(keyword))


    # then make the request
    GBIF_response = requests.get(the_url)

    # method i was writing to project to simplify things
    # def GBIF_search(searchterm):
    #     GBIF_url = "http://api.gbif.org/v1/species/search?q={0}&rank=GENUS&limit=5&language=en".format(searchterm)
    #     #todo error handling here.
    #
    #
    #     #read response stream and extract desired data.
    #     GBIF_response = requests.get(GBIF_url, stream=True)
    #
    #     with open(GBIF_response, 'wb') as out_file:
    #         shutil.copyfileobj(GBIF_response.raw, out_file)
    data = json.loads(GBIF_response.text)
    #print("Here is the data in string format " + str(data))
    return data
# WRITE THAT INFO TO A FILE SO WE DON'T HAVE TO MAKE REPETITIOUS QuERIES FOR PRACTICE DATA.
#def write_to_file():


def get_descript():
    #prints all descriptions returned. Note note all animals returns descriptions
    # for desc in description:
    #     print(str(desc))

    print("Here is the first description" + str(description[0]))
    # convert the results to a dictionary and then extract each results.

            # for number in range(0,4):
            #     if item[unique_keys[number]] in item:
            #         print(item.values)
            #    # print ("Here is the key "  + str(item[unique_keys[number]]))
               # print("Here is the description " + list( item.values()))
        # for description in :
        #     print(description)

        #for item in data['descriptions']:
           # print("Here ia the description")

    #todo obtain access results 2 through 5 i will need to extract differently. Most likely from by class key num

#
#newAnimal = Animal
#newAnimal.Name = 'tiger'
#data = search(newAnimal.Name)
newAnimal.extraction(newAnimal, data)
show_descript()


