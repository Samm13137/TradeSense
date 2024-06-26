import praw
from transformers import pipeline
import bot.settings as settings




reddit = praw.Reddit(
    client_id = settings.REDDIT_ID,
    client_secret = settings.REDDIT_SECRET,
    password = settings.REDDIT_PASS,
    user_agent = "USERAGENT",
    username = settings.REDDIT_USER,
)

# print (reddit)


senti = pipeline('sentiment-analysis', model= "distilbert-base-uncased-finetuned-sst-2-english") 
# "distilbert-base-uncased-finetuned-sst-2-english"
# "nlptown/bert-base-multilingual-uncased-sentiment"  #this has a weird sentiment classification uses a 1-5 star system

def max_character(text):      #this function is to help with like super super long tests so it truncates it to 512 characters
    max_length = 512
    if len(text) > max_length:
        text = text[:max_length]
    return senti(text)


    
for comment in reddit.subreddit("wallstreetbets").stream.comments(): #this is a stream of comments from the subreddit wallstreetbets
    print(f"Comment: {comment.body}")
    try:
        sentiment = max_character(comment.body)
        print(f"Sentiment: {sentiment}")
    except Exception as e:
        print(f"Error analyzing comment: {e}")