import tweepy
from textblob import TextBlob

consumer_key = 'vLd8IjV38qmLLSpxFyEgj2rv0'
consumer_secret = 'isBgQdMaXZ0fKApPY946cmKzeSIxfRbu9GyqE5Wd9GA4ZTfSTi'

access_token = '29699257-AksW0AahKBZ3dvqDj4ls0Iahv3AmlYd5SPhqX2jmW'
access_token_secret = '2VvpU2lZ19E0f01RiWw3JKJGDBSpa73M38ZxJLxeymGJQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print("* Tweet ****************")
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
