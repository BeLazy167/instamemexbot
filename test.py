from instagrapi import Client
from os import environ
import json

username_insta = environ['username_insta']
password_insta = environ['password_insta']
setting = environ['setting']
login_setting = json.loads(setting)
print(type(set))
try:
    cl = Client(login_setting)
    cl.login(username_insta,password_insta)
    print('Login successfully')
except:
    print('login error')
