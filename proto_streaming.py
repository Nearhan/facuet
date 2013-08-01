from twitter import OAuth, TwitterStream
from termcolor import cprint
import os
import sys

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', None)
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN', None)
OAUTH_SECRET = os.environ.get('OAUTH_SECRET', None)

myAuth = OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=myAuth)


def print_resposne(response):
    user_name = response.get('user', {}).get('name')
    time = response.get('created_at')
    tweet = response.get('text')

    cprint(user_name, 'blue')
    cprint(time, 'yellow')
    cprint(tweet, 'green')

#create stream pump out data
argument = sys.argv[1]
stream = twitter_stream.statuses.filter(track=argument)

total_tweets = []
for response in stream:
    if len(total_tweets) <= 1000:
        total_tweets.append(response)
        print_resposne(response)
    else:
        cprint('OVER OVER OVER OVER', 'red')
        sys.exit()
