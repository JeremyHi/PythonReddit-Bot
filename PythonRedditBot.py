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
subreddit = reddit.subreddit('Python')
data = {} #Contains the post data

key = 1
for submission in subreddit.stream.submissions():
  if submission.ups > 20:
    data["Title" + str(key)] = str(submission.title)
    data["OP" + str(key)] = "/u/" + str(submission.author)
    data["URL" + str(key)] = str(submission.url)
    try:
      api.update_status(data["Title" + str(key)] + "\n" + "Subreddit: " + 
        str(subreddit) + "\n" + "Poster: " + data["OP" + str(key)] + "\n" 
        + "#Python #Reddit" + "\n" + str(data["URL" + str(key)]))
    except tweepy.error.TweepError as e:
      ecode = e[0][0]['code']
      if ecode == 186:
        pass
      else:
        raise
    print("POST: " + str(key) + "\n" + data["Title" + str(key)] + "\n" 
      + "Upvotes: " + str(submission.ups))
    key+=1
  time.sleep(60)