import simplejson as json
import twitterSettings

# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = twitterSettings.ACCESS_TOKEN
ACCESS_SECRET = twitterSettings.ACCESS_SECRET
CONSUMER_KEY = twitterSettings.CONSUMER_KEY
CONSUMER_SECRET = twitterSettings.CONSUMER_SECRET

# oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# twitter_stream = TwitterStream(auth = oauth)

# # https://dev.twitter.com/streaming/overview/request-parameters
# iterator = twitter_stream.statuses.filter(language="en", locations="-74,40,-73,41")
# tweetDict = json.dumps(tweet, indent = 4)
# data = {}
# jsondata = json.dumps(data)

# tweet_count = 10
# for tweet in iterator:
#     tweet_count -= 1
#     print json.dumps(tweet, indent = 4)
       
#     if tweet_count <= 0:
#         break

import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def saveStatusToFile(text):
	pass

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
    	print(status.created_at)
        print(status.entities['hashtags'])
    	print(status.text)
    
    def on_error(self, status_code):
     	print "There was an error:",
     	print status_code
     	return False

#myStream = tweepy.Stream(auth = api.auth, listener=tweepy.StreamListener)
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myStream.filter(track=['mcdonalds'])