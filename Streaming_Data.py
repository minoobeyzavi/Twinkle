# Running this code receives the current stream of tweets from the Twitter
# Streaming API and saves it to a local MongoDB database.

try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import pymongo
from pymongo import MongoClient

ACCESS_TOKEN = '716396311650500609-xlnuQgwmfEwFqMk95yIUUP7DpI0A3QV'
ACCESS_SECRET = '6XcRuU520RWH14vrRh8sUI98UCiPJ25q1Cr50Kmx30Q8F'
# Add unique customer key bellow after registering with the twitter API.
CONSUMER_KEY = ''
CONSUMER_SECRET = 'A49FPaTpKxdmboMrsoXzIKqZfWFvJOJCns1ifRrLe4oVkJDPmK'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.sample(language="en")

client = MongoClient()
db = client['tweets_db']

# Choose number of tweets depending on available space.
tweet_count = 1000000

for tweet in iterator:
    tweet_count -= 1
    db.tweets.insert_one(tweet)
    if tweet_count <= 0:
        break
