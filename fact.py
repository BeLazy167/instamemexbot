import requests
import random
from rake_nltk import Rake
import urllib.request as url
from PIL import Image, ImageDraw, ImageFont, ImageOps
import main

ACCESS_KEY_UNSPLASH='j6-TI4_jxVWMUqgKc6K4zgHzFWChSZ6B-q6-cz3mk40'

def key_word():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()['text']
    print(fact)
    r = Rake()
    r.extract_keywords_from_text(fact)
    key_word = r.get_ranked_phrases()
    print(key_word)
    unsplash_img(key_word[0],fact)

def unsplash_img(query,fact):
    print(query)
    orientation=random.choice(['landscape','portrait'])
    path='https://api.unsplash.com/search/photos?&client_id='+ACCESS_KEY_UNSPLASH+'&page=1&query='+query
    print(path)
    response=requests.get(path)
    img_data=response.json()
    print(img_data)
    img_url = img_data['results'][0]['urls']['regular']
    print(img_url)
    img_name ='temp.jpg'
    url.urlretrieve(img_url, img_name)
    image_edit(fact)

def image_edit(fact):
    main.watermark()

    #code for image editing



    main.delete()
key_word()