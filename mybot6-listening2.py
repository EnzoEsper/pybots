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


# What the bot will tweet
filename = open('data/twain.txt', 'r', 1, 'utf-8')
tweet_text = filename.readlines()
filename.close()

# a function that picks a random line number
def line_number():
    return randint(0, len(tweet_text) - 1)

last_tweet = None

def compare_tweets(lasttweet):
    print('comparing tweets...')

    last_tuit = lasttweet
    # gets the most recent tweet by @ocertat and prints its id
    most_recent_tweet = api.user_timeline('EnzoEsper')[0]
    most_recent_tweet = most_recent_tweet.text
    print(f'most recent tweet: {most_recent_tweet}')

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @EnzoEsper
    if most_recent_tweet != last_tuit:
        line = tweet_text[line_number()]
        api.update_status(status=line)
        print('Change detected, tweeting the next line:')
        print(line)
    else:
      print('Nothing change: nothing to tweet.')

    # updates last_tweet to the most_recent_tweet
    time.sleep(10)
    return compare_tweets(most_recent_tweet)

# runs the compare_tweets function every 5 seconds
compare_tweets(last_tweet)

