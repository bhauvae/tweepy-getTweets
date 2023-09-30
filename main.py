# %%
import tweepy

# Add Twitter API key and secret
consumer_key = ""
consumer_secret = ""

# Handling authentication with Twitter
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

# Create a wrapper for the Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True)


# %%
import time


# Helper function for handling pagination in our search and handle rate limits


# Define the term you will be using for searching tweets
query = "#ravelcare"
query = query + " -filter:retweets"

# Define how many tweets to get from the Twitter API
count = 100

# Let's search for tweets using Tweepy
search = tweepy.Cursor(
    api.search_tweets,
    q=query,
    tweet_mode="extended",
    lang="en",
    result_type="recent",
).items(count)

# %%
from transformers import pipeline

# Set up the inference pipeline using a model from the 🤗 Hub
sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

# Let's run the sentiment analysis on each tweet
tweets = []
for tweet in search:
    try:
        content = tweet.full_text
        sentiment = sentiment_analysis(content)
        tweets.append({"tweet": content, "sentiment": sentiment[0]["label"]})

    except:
        pass


# %%
