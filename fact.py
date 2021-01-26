import requests
import random
from rake_nltk import Rake
import urllib.request as url
from PIL import Image, ImageDraw, ImageFont, ImageOps,ImageFilter
import main
import textwrap
from resizeimage import resizeimage

ACCESS_KEY_UNSPLASH='j6-TI4_jxVWMUqgKc6K4zgHzFWChSZ6B-q6-cz3mk40'

var1,var2=0,0
def key_word():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()['text']
    print(fact)
    r = Rake()
    r.extract_keywords_from_text(fact)
    key_word = r.get_ranked_phrases()
    unsplash_img(key_word[0],fact)

def add_border(border, color='white'):
    img = Image.open( 'pixelreset.jpg' )
    if isinstance( border, int ) or isinstance( border, tuple ) :
        bimg = ImageOps.expand( img, border=border, fill=color )  # used to add border
    else :
        raise Exception( "Border is not an integer or tuple!" )
    bimg.save( 'add_border.jpg' )
    return


def image_editor():
    im = Image.open('regular.jpg')  # open image
    if im.size[0] >= im.size[1]:
        whitespace = int((im.size[0] - im.size[1]) / 2) + 0
        xbump = 0
    else:
        xbump = int((im.size[1] - im.size[0]) / 2) + 0
        whitespace = 0
    var1, var2 = whitespace, xbump
    print(var1,var2)
    matted = ImageOps.expand(im, border=(xbump, whitespace),
                             fill='white')
    matted.save("image_editor.jpg")
    matted.show()
    pixelreset()
    return

def pixelreset():
    im=Image.open("image_editor.jpg")
    im=resizeimage.resize_cover(im,[578,578])
    im.save("pixelreset.jpg")
    im.show()
    add_border(10,"white")
    return

def unsplash_img(query,fact):
    orientation=random.choice(['landscape','portrait'])
    path='https://api.unsplash.com/search/photos?&client_id='+ACCESS_KEY_UNSPLASH+'&page=1&query='+query
    print(path)
    response=requests.get(path)
    img_data=response.json()
    img_url = img_data['results'][0]['urls']['regular']
    img_name ='regular.jpg'
    url.urlretrieve(img_url, img_name)
    editor(fact)

def blur():
    im1 = Image.open("add_border.jpg")
    im2 = im1.filter(ImageFilter.GaussianBlur(radius=3))
    im2.save("blur.jpg")
    return "blur.jpg"


def fact_watermark(fact) :
    # Create an Image Object from an Image
    im = Image.open( 'blur.jpg' )
    img_width,img_height = im.size

    draw = ImageDraw.Draw( im )
    text = "@memebot_10101"

    font = ImageFont.truetype( 'arial.ttf', 10)
    textwidth, textheight = draw.textsize( text, font, direction=None, language=None, stroke_width=13 )

    # calculate the x,y coordinates of the text
    margin = 0
    x = img_width - textwidth - margin
    y = 0

    # draw watermark in the top right corner
    draw.text( (x, y), text, fill=2, font=font )
    im.show()

    # Draw in multiple line text
    draw_con = ImageDraw.Draw(im)
    con_font = ImageFont.truetype('arial.ttf', 30)
    textwidth, textheight = draw_con.textsize(fact, con_font, direction=None, language=None, stroke_width=30)
    y_text = (img_height)/2-var1
    lines = textwrap.wrap(fact, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        print(line_width,line_height)
        draw_con.multiline_text((30, y_text),
                  line, font=con_font, fill=(0,0,0),align="center")
        y_text += line_height+20
    im.save("result.jpg")
    return "result.jpg"

def editor(fact):
    # code for editing image
    base = 578
    img = Image.open('regular.jpg')
    width, height = img.size
    if width >= 578:
        wpercent = (base/ float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((base, hsize), Image.ANTIALIAS)
        img.save('regular.jpg')
    image_editor()
    blur()
    fact_watermark(fact)
    main.delete()


key_word()
