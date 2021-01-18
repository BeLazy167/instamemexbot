import praw
import urllib.request
import random
from instabot import Bot
from PIL import Image, ImageDraw, ImageFont
import os
import datetime

random_list = []


try:
    os.remove('temp.jpg')
    os.remove('watermark.jpg')
    os.remove('watermark.jpg.REMOVE_ME')
except:
    None

def random_check():
    page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                 'SaimanSays/', 'wholesomememes']
    to_check = random.choice(page_list)
    if len(random_list) < 6:
        if len(random_list) == 0:
            random_list.append(to_check)
            print(random_list)
            return to_check
        else:
            for pages in random_list:
                if pages==to_check:
                   # print('faied')
                    return random_check()
                else:
                    random_list.append(to_check)
                    print(random_list)
                    return to_check
    else:
        t=0
        for pages in random_list:
            if pages==to_check:
                t=0
                break
            else:
                t=1
                continue
        if t ==1:
            random_list.pop(0)
            random_list.append(to_check)
            print(random_list)
            return to_check
        else :
            #print('faied')
            return random_check()
def meme_installer(target):

    reddit = praw.Reddit(client_id="OZsROIAyH5bAbA", client_secret='PhYFLRgpllL3ZPpdIQe3D5yhRWc', username="DK00167",
                         password="98766789",
                         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

    meme_page = random_check()
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
        return (meme.title,meme_page)
    except:
        meme_installer()


def watermark():

    # Create an Image Object from an Image
    im = Image.open('temp.jpg')
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "@memebot_10101"

    font = ImageFont.truetype('arial.ttf', 30)
    textwidth, textheight = draw.textsize(text, font, direction=None, language=None, stroke_width=20)

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


def insta_upload(title,page):

    username = 'memebot_10101' # your username
    password = 'memebot@10101'  # your password

    image = watermark()  # here you can put the image directory
    final_caption = title + '\n r/' + page + '\n #memes #meme #dankmemes #funnymemes #memesdaily #edgymemes #dankmeme #offensivememes #dailymemes #fortnitememes #memestagram #spicymemes #funnymeme #memepage #memer #btsmemes #memelord #animememes #memez #tiktokmemes #memesespañol #memesespañol #nichememes #dankmemesdaily #edgymeme #memeaccount #kpopmemes #bestmemes #spongebobmemes #darkmemes'

    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(image,final_caption)


while(True):
    if(datetime.datetime.now().strftime("%X") == '23:46:30'):
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
