import simplejson as json
import tweepy
import twitterTokens

ACCESS_TOKEN = twitterTokens.ACCESS_TOKEN
ACCESS_SECRET = twitterTokens.ACCESS_SECRET
CONSUMER_KEY = twitterTokens.CONSUMER_KEY
CONSUMER_SECRET = twitterTokens.CONSUMER_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def openJsonFile(filename):
	jsonObj = open(filename, "r")
	parsedJson = json.load(jsonObj)
	return parsedJson

places = openJsonFile("hunterDB.json")
twitterList = []
noTwitter = []
checkForDupe = []

#append twitter and non twitter names to lists and remove spaces to prepare for searchInput
for place in places:
	if 'twitter' in place['contact']:
		#print place['contact']['twitter']
		twitterList.append(place['contact']['twitter'])
	else:
		noTwitter.append(place['name'].replace(' ', ""))

# print "Places with Twitter:", twitterList
# print "Places with no Twitter:", noTwitter

def hashtagSearch(searchInput):
	tweetList = []
	for tweet in tweepy.Cursor(api.search, q=searchInput, geocode="40.7589,-73.9851,25mi").items(50):
		#tweetText = ''.join([str(tweet.created_at), " ", tweet.text]) #time stamp and tweet contents
		tweetText = ''.join([str(tweet.created_at)]) #time stamp only
		tweetList.append(tweetText)
		print tweetText
	return tweetList

def saveToFile(listOfTweets, locationName):
	localdb = open("localdb2.txt", "a")
	localdb.write("%" + locationName + "\n")
	for tweet in listOfTweets:
		#print tweet
		#localdb.write(tweet.encode('ascii', 'ignore').decode('ascii'))
		localdb.write(tweet.encode('utf-8').strip() + "\n")
	localdb.write("*****\n")

def duplicateRemover(filename):
	lines_seen = set() # holds lines already seen
	outfile = open(filename, "w")
	for line in open(filename, "r"):
    		if line not in lines_seen: # not a duplicate
        		outfile.write(line)
        	lines_seen.add(line)
		outfile.close()

for index, entry in enumerate(twitterList):
	tweets = hashtagSearch(twitterList[index])
	saveToFile(tweets, twitterList[index])
	#print '*************************'

# for index, entry in enumerate(noTwitter):
# 	hashtagSearch(noTwitter[index])
# 	print '*************************'



#duplicateRemover("localdb.txt")






















