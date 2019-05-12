#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MAD LIB MAKER
# This script will generate mad-libs based off of a William Carlos
# poem, 'The Red Wheelbarrow.' Each poem will then be
# tweeted by the bot account. 

import json, io, tweepy, time, urllib3
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


http = urllib3.PoolManager()

response1 =  http.request('GET', 'https://raw.githubusercontent.com/dariusk/corpora/master/data/objects/objects.json' )
response2 =  http.request('GET', 'https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json')
response3 =  http.request('GET', 'https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/occupations.json')

response1read = response1.data.decode()
response2read = response2.data.decode()
response3read = response3.data.decode()

# Create Python-readable lists of items in JSON files
list1 = json.loads(response1read)['objects']
list2 = json.loads(response2read)['menuItems']
list3 = json.loads(response3read)['occupations']


# Repeatable poem-generator
poemlist = []
count = 0

# This script will generate 2 poems, and tweet them all 10 seconds apart. 
while count < 2: 
    # Picks random numbers
    num1 = randint(0, len(list1) - 1)
    num2 = randint(0, len(list2) - 1)
    num3 = randint(0, len(list3) - 1)

    # Chooses random items from each list using random numbers
    first = list1[num1]
    second = list2[num2].lower()
    third = list3[num3].lower() + 's'

    # Fills in the blanks of the poem
    poem = f'so much depends\nupon\n\na\n{first}\n\nglazed with\n{second}\n\nbeside the\n{third}\n\n'

    print(poem)
    poemlist.append(poem) # Adds poem to long list of poems
    count += 1


# Line up tweets for bot
for line in poemlist: 
    api.update_status(status=line)
    #print line 
    time.sleep(10) # Sleep for 10 seconds


print('ALL DONE!')