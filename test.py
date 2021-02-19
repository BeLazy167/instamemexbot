from instabot import Bot
from os import environ

username_insta = environ['username_insta']
password_insta = environ['password_insta']

bot=Bot()
bot.login(username=username_insta,password=password_insta)