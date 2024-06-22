from twikit import Client
from transformers import pipeline
import bot.settings as settings
import time

client = Client('en-US')
client.login(
    auth_info_1=settings.TWITTER_USERNAME,
    auth_info_2=settings.TWITTER_EMAIL,
    password=settings.TWITTER_PASSWORD
)

senti = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def max_character(text):
    max_length = 512
    if len(text) > max_length:
        text = text[:max_length]
    return senti(text)

def get_live_tweets(keywords):
    while True:
        try:
            for keyword in keywords:
                tweets = client.search_tweet(keyword, 'Latest')
                for tweet in tweets:
                    print(f"Keyword: {keyword} | Tweet: {tweet.text}")
                    try:
                        sentiment = max_character(tweet.text)
                        print(f"Sentiment: {sentiment}")
                    except Exception as e:
                        print(f"Error analyzing tweet: {e}")
                time.sleep(60) 
        except Exception as e:
            if '429' in str(e):
                print("rate limit very sad ;(")
                time.sleep(15 * 60)  
            else:
                print(f"bad request error fetching tweets: {e}")
                time.sleep(60) 

if __name__ == "__main__":
    keywords = ['stocks', 'Bitcoin', 'AAPL']  #idk aadd any m ore keywords u seem deemed fit to help with the sentiment analysis
    get_live_tweets(keywords)
