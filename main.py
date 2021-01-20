import praw
import urllib.request
import random
from instabot import Bot
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import datetime

try:
    os.remove('temp.jpg')
    os.remove('watermark.jpg')
    os.remove('watermark.jpg.REMOVE_ME')
except:
    None


def meme_installer(target):
    reddit = praw.Reddit(client_id="OZsROIAyH5bAbA", client_secret='PhYFLRgpllL3ZPpdIQe3D5yhRWc', username="DK00167",
                         password="98766789",
                         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
    page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                 'SaimanSays/', 'wholesomememes']
    meme_page = random.choice(page_list)
    memes = reddit.subreddit(meme_page)

    if target == 1:
        day_meme = memes.top('day')
    elif target == 2:
        day_meme = memes.top('week')
    for meme in day_meme:
        break
    try:
        fullname = 'temp' + '.jpg'
        urllib.request.urlretrieve(meme.url, fullname)
        return (meme.title, meme_page)
    except:
        meme_installer()


def add_border(border=50, color='white'):
    img = Image.open('temp.jpg')

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color) #used to add border
    else:
        raise Exception("Border is not an integer or tuple!")
    bimg.save('temp.jpg')

def image_editor():
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


def insta_upload(title, page):
    username = 'memebot_10101'  # your username
    password = 'memebot@10101'  # your password

    image = watermark()  # here you can put the image directory
    final_caption = title + '\n r/' + page + '\n #memes #meme #dankmemes #funnymemes #memesdaily #edgymemes #dankmeme #offensivememes #dailymemes #fortnitememes #memestagram #spicymemes #funnymeme #memepage #memer #btsmemes #memelord #animememes #memez #tiktokmemes #memesespañol #memesespañol #nichememes #dankmemesdaily #edgymeme #memeaccount #kpopmemes #bestmemes #spongebobmemes #darkmemes'

    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(image, final_caption)


while(True):
    if(datetime.datetime.now().strftime("%X") == '10:30:00'):
        try:
            if(datetime.datetime.now().strftime("%X") == 'Wednesday'):
                title , page = meme_installer(target=2)
                insta_upload(title,page)
                print('sunday fun')
            else:
                title, page = meme_installer(target=1)
                insta_upload(title, page)
                print('normal meme upload on' + (datetime.datetime.now().strftime("%A")))
        except :
            continue
    else:
        print(datetime.datetime.now().strftime("%X"))
    try:
        os.remove('temp.jpg')
        os.remove('watermark.jpg')
        os.remove('watermark.jpg.REMOVE_ME')
    except:
        None