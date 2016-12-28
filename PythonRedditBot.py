#!/usr/bin/python
import praw

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