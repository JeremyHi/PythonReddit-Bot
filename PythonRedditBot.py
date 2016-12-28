import praw, tweepy, time, sys
from pyshorteners import Shortener

tokenFile = "TwitterInfo.txt" #file containing OAuth infomation
filename = open(tokenFile,'r')
f = filename.readlines()
filename.close()
keys = [] #keys in order for use below

for line in f:
	keys.append(line[:-1])

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]
api_key = keys[4]
shortener = Shortener('Google', api_key=api_key)	
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit('bot1')
subreddit = reddit.front
data = {} #Contains the post data

for submission in subreddit.hot(limit=1):
	data["Title"] = str(submission.title)
	data["Author"] = "/u/" + str(submission.author)
	data["URL"] = str(submission.url)
	api.update_status(data["Title"] + "\n" + "Subreddit: " + 
		str(subreddit) + "\n" + str(shortener.short(data["URL"])))
	time.sleep(12)