#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 3

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('data/twain.txt', 'r', 1 , 'utf-8')
tweet_text = filename.readlines()  #create an array with each line of the .txt
filename.close()

# loop through the tweet_text
for line in tweet_text[0:5]: # Will only write first 5 lines
    next_line = line.strip() # strip retorna una copia de cada linea en la cual se remueve (en el principio y al final) del string el parametro pasado, en este caso /n
    api.update_status(status=next_line)
    print(next_line)
    time.sleep(10) # Sleep for 10 seconds

print("All done!")

# To quit early: CTRL+C and wait a few seconds
