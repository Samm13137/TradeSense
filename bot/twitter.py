import settings as settings
import tweepy as t

class TwitterScraper:

    def __init__(self):
            self.login()

    def login(self):
        consumer_key = settings.TWITTER_API_KEY
        consumer_secret = settings.TWITTER_API_KEY_SECRET
        access_token = settings.TWITTER_ACCESS_KEY
        access_token_secret = settings.TWITTER_ACCESS_KEY_SECRET
        auth = t.OAuth1UserHandler(
             consumer_key, 
             consumer_secret, 
             access_token, 
             access_token_secret
             )
        self.api = t.API(auth, wait_on_rate_limit=True)

    def get_tweets(self, keyword, count, date_since=None):
        tweets = t.Cursor(self.api.search_tweets, q=keyword, lang='en').items(count)
        tweet_list = [[tweet.text, tweet.created_at] for tweet in tweets]

        for tweet in tweet_list:
            print(tweet)
        return tweet_list
    

test = TwitterScraper()
test.get_tweets("stock", 5)