#!/usr/bin/env python
# -*- coding: utf-8 -*-

# THIS BOTS TWEETS OUT RANDOM ITEMS FROM A CSV FILE

# Housekeeping: do not edit
import tweepy, time, csv
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('data/az_database_list.csv', 'r', 1, 'utf-8')
csv_data = csv.reader(filename)
csv_list = list(csv_data)
filename.close()
count = 0

# create a continuous loop that iterates five times
while count <5:
    # select a random item from the csv_list
    random_integer = randint(1, len(csv_list) - 1)
    csv_list_item = csv_list[random_integer]

    # compose the tweet
    tweet = csv_list_item[1] + ' : ' + csv_list_item[2]

    # check to make sure the tweet is not too many characters
    # and if it's too long, shorten it!
    if len(tweet) > 279:
        tweet = tweet[0:276] + '...'

    # post the tweet and print it to the console
    api.update_status(status=tweet)
    print(tweet)

    count += 1
    # wait 10 seconds before repeating
    time.sleep(10)


# To quit before the count reachs five: press CTRL+C and wait a few seconds
