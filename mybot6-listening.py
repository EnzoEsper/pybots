#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This bot listens to the account @EnzoEsper, and when that account
# tweets, it responds with a line of Twain
import tweepy, time
from credentials import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# initially, the script will assume that the last tweet was a null value
last_tweet = None

# What the bot will tweet
filename = open('data/twain.txt', 'r', 1, 'utf-8')
tweet_text = filename.readlines()
filename.close()

# a function that picks a random line number
def line_number():
    return randint(0, len(tweet_text) - 1)

def compare_tweets():
    # uses the global lasttweet variable, rather than the local one.
    # (it's probably best practice not to use a global variable for
    # this purpose, but we've shown this approach for its readability.)
    print('comparing tweets...')
    global last_tweet

    # gets the most recent tweet by @EnzoEsper and prints its 
    most_recent_tweet = api.user_timeline('EnzoEsper')[0]
    most_recent_tweet = most_recent_tweet.text
    print(f'most recent tweet: {most_recent_tweet}')

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @EnzoEsper
    if most_recent_tweet != last_tweet:
        line = tweet_text[line_number()]
        api.update_status(status=line)
        print('Change detected, tweeting the next line:')
        print(line)
    else:
      print('Nothing change: nothing to tweet.')

    # updates last_tweet to the most_recent_tweet
    last_tweet = most_recent_tweet

# runs the compare_tweets function every 10 seconds
while True:
    compare_tweets()
    time.sleep(10)  

