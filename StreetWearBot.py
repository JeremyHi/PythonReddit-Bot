import praw, tweepy, time, sys

tokenFile = "TwitterInfoStreetwear.txt" #file containing OAuth infomation
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
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit('bot2')
subreddit = reddit.subreddit('Streetwear')
data = {} #Contains the post data

key = 1
for submission in subreddit.stream.submissions():
  if submission.ups > 50:
    data["Title" + str(key)] = str(submission.title) if len(str(submission.title)) <= 50 else (str(submission.title)[:50] + "...")
    data["OP" + str(key)] = "/u/" + str(submission.author)
    data["URL" + str(key)] = str(submission.url)
    print("POST: " + str(key) + "\n" + data["Title" + str(key)] + "\n" 
    + "Upvotes: " + str(submission.ups))
    api.update_status(data["Title" + str(key)] + "\n" + "Poster: " + data["OP" + str(key)] + "\n" 
      + "#Streetwear #Reddit" + "\n" + str(data["URL" + str(key)]))
    key+=1
  time.sleep(600)