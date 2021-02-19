import datetime
import os
import random
from instagrapi import Client
import urllib.request
import re
import json
import praw
from PIL import Image, ImageDraw, ImageFont, ImageOps
# from instabot import Bot
from resizeimage import resizeimage
from os import environ

client_id = environ['client_id']
client_secret = environ['client_secret']
username = environ['username']
password = environ['password']
username_insta = environ['username_insta']
password_insta = environ['password_insta']

random_list = []
random_list_full = []

try:
    setting = environ['setting']
    login_setting = json.loads(setting)
    cl = Client(login_setting)
    cl.login(username_insta, password_insta)
    print('login successful')
except:
    print("login error")


def file_to_list():
    with open("listofpages.txt", "r") as listofpages:
        lines = listofpages.readlines()
    random_list_full_without_n = [element.strip() for element in lines]
    random_list = random_list_full_without_n[-6:]
    return random_list


def delete():
    os.remove('meme.jpg')
    os.remove('meme_watermark.jpg')


def random_check(random_list):
    page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                 'SaimanSays/', 'wholesomememes', 'IndianMeyMeys', 'indiameme', 'desimemes', 'Tinder', '2meirl4meirl',
                 'ComedyCemetery', 'terriblefacebookmemes']
    to_check = random.choice(page_list)
    random_list = file_to_list()
    f = open("listofpages.txt", "a")
    if len(random_list) < 6:
        if len(random_list) == 0:
            random_list.append(to_check)
            to_write = to_check + "\n"
            f.write(to_write)
            return to_check
        else:
            for pages in random_list:
                if pages == to_check:
                    # print('faied')
                    return random_check(random_list)
                else:
                    random_list.append(to_check)
                    to_write = to_check + "\n"
                    f.write(to_write)
                    return to_check
    else:
        t = 0
        for pages in random_list:
            if pages == to_check:
                t = 0
                break
            else:
                t = 1
                continue
        if t == 1:
            random_list.pop(0)
            random_list.append(to_check)
            to_write = to_check + "\n"
            f.write(to_write)
            return to_check
        else:
            # print('faied')
            return random_check(random_list)


def meme_installer(target):
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username,
                         password=password,
                         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

    meme_page = random_check(random_list)
    memes = reddit.subreddit(meme_page)

    if target == 1:
        day_meme = memes.top('week')
    elif target == 2:
        day_meme = memes.top('month')
    for meme in day_meme:
        if re.search("^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg)$", meme.url):
            break

    try:
        fullname = 'meme' + '.jpg'
        urllib.request.urlretrieve(meme.url, fullname)
        return (meme.title, meme_page)
    except:
        meme_installer()


def add_border(border, color='white'):
    img = Image.open('meme.jpg')

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color)  # used to add border
    else:
        raise Exception("Border is not an integer or tuple!")
    bimg.save('meme.jpg')


def image_editor():
    img = Image.open('meme.jpg')
    # below code is used to make image width/height ratio 1.0 # open image
    width, height = img.size
    if img.size[0] >= img.size[1]:
        whitespace = int((img.size[0] - img.size[1]) / 2) + 0
        xbump = 0
    else:
        xbump = int((img.size[1] - img.size[0]) / 2) + 0
        whitespace = 0
    matted = ImageOps.expand(img, border=(xbump, whitespace),
                             fill='white')  # used to add white space to image in ratio=1(ratio=width/height)

    # resize image to 1070x1070
    w, h = matted.size
    print(w, h)
    if w > h:
        im = resizeimage.resize_cover(matted, [w - 1, h])
        im.save("meme.jpg")
        add_border(5, "white")  # used to add white border
    elif h > w:
        im = resizeimage.resize_cover(matted, [w, h - 1])
        im.save("meme.jpg")
        add_border(5, "white")  # used to add white border
    else:
        im = resizeimage.resize_cover(matted, [w, h])
        im.save("meme.jpg")
        add_border(5, "white")  # used to add white border
    return 'meme.jpg'


def watermark():
    # Create an Image Object from an Image
    image_editor()
    im = Image.open('meme.jpg')
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "@_memebot_10101"

    font = ImageFont.truetype('/app/.fonts/Ts.ttf', 20)
    textwidth, textheight = draw.textsize(text, font, direction=None, language=None, stroke_width=13)

    # calculate the x,y coordinates of the text
    x = width - textwidth
    y = 0

    # draw watermark in the bottom right corner
    draw.text((x, y), text, fill=2, font=font)
    im.show()

    # Save watermarked image
    im.save('meme_watermark.jpg')
    return 'meme_watermark.jpg'


def send_message(message):
    # send message to to conform that post is uploaded
    user_id_1 = cl.user_id_from_username('iamjaypanchal_')
    user_id_2 = cl.user_id_from_username('be__lazy')
    cl.direct_send(text=message, user_ids=[user_id_1, user_id_2])
    return


def insta_upload_meme(title, page):
    image = watermark()  # here you can put the image directory
    final_caption = title + '\n r/' + page + '.\n.\n.\n.\n.\n #memes #meme #dankmemes #funnymemes #memesdaily #edgymemes #dankmeme #offensivememes #dailymemes #fortnitememes #memestagram #spicymemes #funnymeme #memepage #memer #btsmemes #memelord #animememes #memez #tiktokmemes #memesespañol #memesespañol #nichememes #dankmemesdaily #edgymeme #memeaccount #kpopmemes #bestmemes #spongebobmemes #darkmemes'
    cl.photo_upload(image, caption=final_caption)
    send_message('meme is uploaded')
    #
    # bot = Bot( )
    # bot.login( username=username_insta, password=password_insta,is_threaded=True)
    # bot.upload_photo( image, final_caption )


def full_run():
    if (datetime.datetime.now().strftime("%X") == 'Wednesday'):
        title, page = meme_installer(target=2)
        insta_upload_meme(title, page)
        print('sunday fun')
    else:
        title, page = meme_installer(target=1)
        insta_upload_meme(title, page)
        print('normal meme upload on' + (datetime.datetime.now().strftime("%A")))
    delete()
