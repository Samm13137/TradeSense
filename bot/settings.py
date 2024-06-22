import os
from dotenv import load_dotenv

# loads in our api keys from .env to keep them private. 
# .env is for the OS and it is kept local/private when you upload to git.

load_dotenv()


REDDIT_ID = os.getenv('REDDIT_ID')

REDDIT_SECRET = os.getenv('REDDIT_SECRET')

REDDIT_USER = os.getenv('REDDIT_USER')

REDDIT_PASS = os.getenv('REDDIT_PASS')

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')

TWITTER_API_KEY_SECRET = os.getenv('TWITTER_API_KEY_SECRET')

TWITTER_BEARER_KEY = os.getenv('TWITTER_BEARER_KEY')

TWITTER_ACCESS_KEY = os.getenv('TWITTER_ACCESS_KEY')

TWITTER_ACCESS_KEY_SECRET = os.getenv('TWITTER_ACCESS_KEY_SECRET')



TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')


TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')


TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')