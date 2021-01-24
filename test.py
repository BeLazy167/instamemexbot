import requests
import random
from rake_nltk import Rake
import urllib.request as url
from PIL import Image, ImageDraw, ImageFont, ImageOps

ACCESS_KEY_UNSPLASH='j6-TI4_jxVWMUqgKc6K4zgHzFWChSZ6B-q6-cz3mk40'

def key_word():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()['text']
    print(fact)
    r = Rake(max_length=1)
    r.extract_keywords_from_text(fact)
    key_word = r.get_ranked_phrases()[0]
    print(key_word)
    return key_word

def unsplash_img(query):
    orientation=random.choice(['landscape','portrait'])
    path='https://api.unsplash.com/search/photos?&client_id='+ACCESS_KEY_UNSPLASH+'&page=1&query='+query
    print(path)
    response=requests.get(path)
    img_data=response.json()
    print(img_data)
    img_url = img_data['results'][0]['urls']['regular']
    print(img_url)
    img_author = img_data['results'][0]['user']['name']
    print(img_author)
    img_name ='temp.jpg'
    url.urlretrieve(img_url, img_name)

def add_border(border=50, color='white'):
    img = Image.open('temp.jpg')

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color) #used to add border
    else:
        raise Exception("Border is not an integer or tuple!")
    bimg.save('temp.jpg')

def image_editor():
    query=key_word()
    unsplash_img(query)
    im = Image.open('temp.jpg')# open image
    width, height = im.size
    if im.size[0] >= im.size[1]:
        whitespace = int((im.size[0] - im.size[1]) / 2) + 0
        xbump = 0
    else:
        xbump = int((im.size[1] - im.size[0]) / 2) + 0
        whitespace = 0
    matted = ImageOps.expand(im, border=(xbump, whitespace), fill='white') #used to add white space to image in ratio=1(ratio=width/height)
    matted.save('temp.jpg')
    add_border(17,'white') # used to add white border

def watermark():
    # Create an Image Object from an Image
    image_editor()
    im = Image.open('temp.jpg')
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "@memebot_10101"

    font = ImageFont.truetype('arial.ttf', 20)
    textwidth, textheight = draw.textsize(text, font, direction=None, language=None, stroke_width=13)

    # calculate the x,y coordinates of the text
    margin = 0
    x = width - textwidth - margin
    y = 0

    # draw watermark in the bottom right corner
    draw.text((x, y), text, fill=2, font=font)
    im.show()

    # Save watermarked image
    im.save('watermark.jpg')
    return 'watermark.jpg'

watermark()








