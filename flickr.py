import requests
import urllib
import json
import shutil


photoUrl_list = []
json_resp = ""




def ask():
    animalName = input("Enter the name of an animal to search for photos")
    return str(animalName)


# flickr api address
def make_flickr_query(animalName):

    flickerSearchURL = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=920322c4d9cb2198bab884879c0a9546&tags={0}&format=json&nojsoncallback=1'.format(animalName)

    flickrResponse = urllib.request.urlopen(flickerSearchURL)

    #get json back need to decode it to retrieve data
    flickrResponseJSONString = flickrResponse.read().decode('UTF-8')
    # then load it into json format to extract data
    flickrResponseJson = json.loads(flickrResponseJSONString)


    # loop over the photo responses and collect 5 photos.
    for animal_num in range(0, 5):
        jsonforphoto = flickrResponseJson['photos']['photo'][animal_num]
     

        #Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
        #https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

        # phrases we need to request each photo
        secret = jsonforphoto['secret']
        id = jsonforphoto['id']
        server = jsonforphoto['server']
        farm = jsonforphoto['farm']

        print(jsonforphoto)  #Just checking we get the JSON we expect
        #TODO add error handing

        #format the link needed for the photo url to be sent to flickr
        fetchPhotoURL = 'https://farm%s.staticflickr.com/%s/%s_%s_m.jpg' % (farm, server, id, secret)
        # as they are created add them to a list to later retieve photos by specs provided
        photoUrl_list.append(fetchPhotoURL)
        #print(fetchPhotoURL)   #Again, just checking

        #Reference: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
        animalName = 'animal'
        animal_responseFileNameJpg = animalName + str(animal_num) + '.jpg'

        #Read the response and save it as a .jpg. Use shutil to copy the stream of bytes into a file
        # http://preshing.com/20110920/the-python-with-statement-by-example/
        # todo NOTE that this is a stream, see if there are other ways i can utilize the stream feature to do different things.
        # this is where it actually makes the request.
        resp = requests.get(fetchPhotoURL, stream=True)

        with open(animal_responseFileNameJpg, 'wb') as out_file:
               #todo look into shutils to see what it is???  <<~~~~~~~
               # my guess is that it reads the response and turns it into the gif format as a new file save.
               # the output is the file with the name created above
                shutil.copyfileobj(resp.raw, out_file)
                #img = Image
                #img.Image.show()
                del resp
        #return photoUrl_list


def show_links():
    for href in photoUrl_list:
        print("is there a list here ?" + str(href))
# example of a line response from flickr https://farm2.staticflickr.com/1616/25720443592_e778886425_m.jpg

            #TODO tweak the url maybe search for photos that have a lot of likes that match the animal species, also sort by interesting. ???



# q = ask()
# json_resp = make_flickr_query(q)
# show_links()


