import os
from dotenv import load_dotenv

# loads in our api keys from .env to keep them private. 
# .env is for the OS and it is kept local/private when you upload to git.

load_dotenv()


REDDIT_ID = os.getenv('REDDIT_ID')

REDDIT_SECRET = os.getenv('REDDIT_SECRET')

REDDIT_USER = os.getenv('REDDIT_USER')

REDDIT_PASS = os.getenv('REDDIT_PASS')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')