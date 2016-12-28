#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw, tweepy, time, sys

tokenFile = "TwitterInfo.txt" #file containing OAuth infomation, 1 line at a time
filename = open(tokenFile,'r')
f = filename.readlines()
filename.close()
keys = []

for line in f:
	keys.append(line[:-1])

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit('bot1')
netsec = reddit.subreddit("netsec")
data = {}

key = 1
for submission in netsec.new(limit=1):
	data["Title" + str(key)] = str(submission.title)
	data["URL" + str(key)] = str(submission.url)
	data["Author" + str(key)] = "/u/" + str(submission.author)
	#key+=1

print(data)