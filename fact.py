import requests
from rake_nltk import Rake
import urllib.request as url
from PIL import Image, ImageDraw, ImageFont, ImageOps,ImageFilter
import textwrap
from resizeimage import resizeimage
from instabot import Bot
import os

ACCESS_KEY_UNSPLASH='j6-TI4_jxVWMUqgKc6K4zgHzFWChSZ6B-q6-cz3mk40'
var1=0
title=''

def key_word():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()['text']
    print(fact)
    r = Rake()
    r.extract_keywords_from_text(fact)
    key_word = r.get_ranked_phrases()
    print(key_word)
    title=key_word[0]
    unsplash_img(fact,key_word[0])
    return "temp.jpg",title

def unsplash_img(fact,query="fact"):
    print(query)
    path='https://api.unsplash.com/search/photos?&client_id='+ACCESS_KEY_UNSPLASH+'&page=1&query='+query+'&orientation=landscape'
    print(path)
    response=requests.get(path)
    img_data=response.json()
    img_url = img_data['results'][0]['urls']['regular']
    print(img_url)
    img_name ='temp.jpg'
    url.urlretrieve(img_url, img_name)
    editor(fact)

def editor(fact):
    base = 1070
    img = Image.open('temp.jpg')
    width, height = img.size
    if width >= 1070:
        wpercent = (base/ float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((base, hsize), Image.ANTIALIAS)
        img.save('temp.jpg')
    image_editor()
    fact_watermark(fact)

def image_editor():
    im = Image.open('temp.jpg')  # open image
    if im.size[0] >= im.size[1]:
        whitespace = int((im.size[0] - im.size[1]) / 2) + 0
        xbump = 0
    else:
        xbump = int((im.size[1] - im.size[0]) / 2) + 0
        whitespace = 0
    var1 = whitespace
    matted = ImageOps.expand(im, border=(xbump, whitespace),
                             fill='white')

    # resize image to 1070x1070
    im = resizeimage.resize_cover(matted, [1070,1070])
    im.save("temp.jpg")
    add_border_and_blur(5, "white")
    return

def add_border_and_blur(border, color='white'):
    img = Image.open( 'temp.jpg' )
    if isinstance( border, int ) or isinstance( border, tuple ) :
        bimg = ImageOps.expand( img, border=border, fill=color )  # used to add border
    else :
        raise Exception( "Border is not an integer or tuple!" )

    im2 = bimg.filter(ImageFilter.GaussianBlur(radius=3))
    im2.save("temp.jpg")
    return

def fact_watermark(fact) :
    # Create an Image Object from an Image
    im = Image.open( 'temp.jpg' )
    img_width,img_height = im.size

    draw = ImageDraw.Draw( im )
    text = "@factbot_10101"

    font = ImageFont.truetype( 'arial.ttf', 20)
    textwidth, textheight = draw.textsize( text, font, direction=None, language=None, stroke_width=13 )

    # calculate the x,y coordinates of the text
    margin = 0
    x = img_width - textwidth - margin
    y = 0

    # draw watermark in the top right corner
    draw.text( (x, y), text, fill=2, font=font )

    # Draw in multiple line text
    draw_con = ImageDraw.Draw(im)
    con_font = ImageFont.truetype('Font/Ts.ttf', 60)
    lines = textwrap.wrap(fact, width=37)
    new_fact='\n'.join(lines)
    w,h=con_font.getsize(new_fact)
    space=20
    y_text = (img_height) / 2 - var1 - ((int((h+space))*len(lines)/ 2)) + 30
    draw_con.multiline_text((35, y_text),new_fact, font=con_font, fill=(0,0,0),spacing=space,stroke_width=3,stroke_fill=(255,255,255))
    im.save("temp.jpg")
    return "temp.jpg"

def delete():
    try:
        os.remove('temp.jpg')
        os.remove('temp.jpg.REMOVE_ME.jpg')
    except:
        print("nothing is deleted")

def insta_upload_fact():
    print("Input your instagram username and password to upload fact")
    username = 'factbot__'# your username
    password = 'jay2345' # your password

    image,title = key_word()  # here you can put the image directory
    final_caption = title +' \n #fact #facts #knowledge #didyouknow #factz #factsdaily #amazingfacts #factsoflife #love #science #dailyfacts #knowledgeispower #india #gk #generalknowledge #instafacts #instagram #interestingfacts #funfacts #follow #truefacts #life #factoftheday #coolfacts #sciencefacts #motivation #truth #didyouknowfacts #quotes #bhfyp'

    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(image, final_caption)

insta_upload_fact()
delete()

