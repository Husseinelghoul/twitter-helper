import configparser
from datetime import datetime

import tweepy

# Read the Twitter API keys and access tokens from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

consumer_key = config["Twitter"]["consumer_key"]
consumer_secret = config["Twitter"]["consumer_secret"]
access_token = config["Twitter"]["access_token"]
access_token_secret = config["Twitter"]["access_token_secret"]

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Set the start and end dates for the unlike operation
start_date = datetime(2023, 1, 1, 0, 0, 0)  # Change to your desired start date
end_date = datetime(2023, 5, 9, 23, 59, 59)  # Change to your desired end date

# Get all the tweets the user has liked
liked_tweets = api.favorites()

# Unlike each tweet that was liked between the start and end dates
for tweet in liked_tweets:
    if start_date <= tweet.created_at <= end_date:
        try:
            api.destroy_favorite(tweet.id)
            print(f"Unliked tweet: {tweet.id} - {tweet.created_at}")
        except tweepy.TweepError as e:
            print(f"Error unliking tweet {tweet.id}: {e}")
