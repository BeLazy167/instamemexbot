from instagrapi import Client
from os import environ

username_insta = environ['username_insta']
password_insta = environ['password_insta']
setting = environ['setting']
print(type(setting))
try:
    cl = Client(setting)
    cl.login(username_insta,password_insta)
    print('Login successfully')
except:
    print('login error')
