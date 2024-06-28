from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from transformers import pipeline


# tickers = ['AMZN', 'AMD', 'NVDA', 'FB'] # Ticker symbols that are parsed for

def get_parsed_data(tickers): # Scraps for parsed data. Takes in an array of tickers
    finviz_url = 'https://finviz.com/quote.ashx?t=' # base url
    parsed_data = [] # an array of arrays with structure [Ticker | Date | Time | Title]
    news_tables = {} # A dictionary of news tables used for parsing data
    for ticker in tickers:
        url = finviz_url + ticker # finds URL to parse from

        req = Request(url=url, headers={'user-agent': 'tradesense'})
        response = urlopen(req)

        html = BeautifulSoup(response, features="html.parser") # rips the HTML from response
        news_table = html.find(id='news-table') # scraps the table of news articles from website
        news_tables[ticker] = news_table

        break

    for ticker, news_table in news_tables.items():
        for row in news_table.findAll('tr'):
            if row.a: # Avoids error with articles. Basically checks if a title exists
                title = row.a.text # Scrapes title
                date_data = row.td.text.strip().split(' ') # Scrapes date/time. Not all have a date but all have time
                if len(date_data) == 1:
                    time = date_data[0]
                else:
                    date = date_data[0] 
                    time = date_data[1]
                parsed_data.append([ticker, date, time, title])

    return parsed_data


def max_character(text):      #this function is to help with like super super long tests so it truncates it to 512 characters
    max_length = 512
    senti = pipeline('sentiment-analysis', model= "distilbert-base-uncased-finetuned-sst-2-english") 
    # "distilbert-base-uncased-finetuned-sst-2-english"
    # "nlptown/bert-base-multilingual-uncased-sentiment"  #this has a weird sentiment classification uses a 1-5 star system
    if len(text) > max_length:
        text = text[:max_length]
    return senti(text)


def analyze(parsed_data): # Runs senti analysis on parsed data
    for data in parsed_data:
        print(f"Comment: {data[3]}")
        try:
            sentiment = max_character(data[3])
            print(f"Sentiment: {sentiment}")
        except Exception as e:
            print(f"Error analyzing comment: {e}")

data = get_parsed_data(['AMZN', 'AMD', 'NVDA', 'FB'])
analyze(data)