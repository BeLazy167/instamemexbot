# Instamemexbot

[![GitHub issues](https://img.shields.io/github/issues/BeLazy167/instamemexbot)](https://github.com/BeLazy167/instamemexbot/issues)
[![GitHub license](https://img.shields.io/github/license/BeLazy167/instamemexbot)](https://github.com/BeLazy167/instamemexbot/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/BeLazy167/instamemexbot)](https://github.com/BeLazy167/instamemexbot/stargazers)

## About
**Instamemexbot** is bot which automatically post Memes and Facts on Instagram . The bot posts top Memes from Reddit pages. Bot also post amazing facts and photographs linked with a keyword from the facts.

### Go ahead and follow [@_memebot_10101](https://www.instagram.com/_memebot_10101) on Instagram for amazing Memes and Facts.
<a href="https://www.instagram.com/_memebot_10101" target="blank"><img align="left" src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="_memebot_10101"/></a><br>

## How it works and what it does?
➡️ For Memes, It uses the PRAW – Python Reddit API Wrapper and fetches Memes Images from the different [Reddit](https://www.reddit.com/) Pages.

➡️ On fectching Meme image from reddit, using Pillow library the image is edited to make image ratio 1.0 and watermark is added at top right corner. As the editing is complete it saves the image and is then posted on Instagram using [Instabot](https://pypi.org/project/instabot/) package.

➡️ For facts, It uses the [Random useless facts API](https://uselessfacts.jsph.pl/)

➡️ On fetching the fact it is parsed through [Rapid Automatic Keyword Extraction algorithm](https://github.com/csurfer/rake-nltk) (Rake-nltk) which gives a keyword from the fact . The extracted keyword is then passed to unsplash api for searching that relevant picture for the fact. 

➡️ After receiveing all the metrics and image, using Pillow library the image is edited with the fact and a watermark. As the editing process is complete it saves the image and is then posted on Instagram using [Instabot](https://pypi.org/project/instabot/) package.

➡️ The bot is deployed via Heroku and scheduled to run at intervals using Herokuscheduler.

## Architecture
```
├── LICENSE
├── Procfile
├── README.md
├── .fonts
│   └── Ts.ttf
├── listofpages.txt
├── requirements.txt
├── nltk.txt
├── runtime.txt
├── randmness_checker.py
├── fact.py
├── meme.py
├── main.py
```

### Requirements
- instabot
- Rake-nltk
- Urllib3
- Pillow
- resizeimage
- Python==3.6
- Reddit API, Unsplash API, Useless facts API

### Contributions
Always open for new features just create an issue. If want to add a new feature via pull request please fork and make a separate branch for it.
 > If you want to run it locally
 ```
 git clone https://github.com/marclave/InstaBot.git
 ```
 >run the following command to install the required libraries:
 ```
 pip install -r requirements.txt
 ```

 >add your Instagram creadentials, Unsplash keys 🔑 in fact.py and Reddit keys 🔑 in meme.py. To run the bot first you have to change Time in main.py after changing time run     following command in command prompt
 ```
 python main.py
 ```
 >If you are using any IDE then run main.py


## If you liked our work considering giving it a 🌟.


## Contributers

people who already contributed to Instamemexbot

<a href="https://github.com/BeLazy167/instamemexbot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=BeLazy167/instamemexbot" />
</a>

