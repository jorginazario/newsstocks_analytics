#Tweepy
import tweepy
import sys
import jsonpickle
import os

import matplotlib.pyplot as plt
import numpy as np

# Replace the API_KEY and API_SECRET with your application's key and secret.

API_KEY = 'rF1UhAhVJsmie822K1bXN5lvd'
API_SECRET = 'UykH43jgHn5SWYHTprLyfrQPWKl7V2ODu2MhJVTqIJosjbLn5a'
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,	  wait_on_rate_limit_notify=True)

tweetArr= [0,0,0,0,0,0]

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code

searchQuery = '#Tesla'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.
from_date = '2017-04-16'
to_date = '2017-04-17'


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1L

for x in range (0,6):
	tweetCount = 0
	print("Downloading max {0} tweets".format(maxTweets))
	with open(fName, 'w') as f:
	    while tweetCount < maxTweets:
	        try:
        	    if (max_id <= 0):
                	if (not sinceId):
	                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since=from_date , until=to_date)#, result_type = 'popular')
        	        else:
                	    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId, since=from_date , until=to_date)#, result_type = 'popular')
	            else:
        	        if (not sinceId):
                	    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                        	                    max_id=str(max_id - 1), since=from_date , until=to_date)#, result_type = 'popular')
	                else:
        	            new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                	                            max_id=str(max_id - 1),
                        	                    since_id=sinceId, since=from_date , until=to_date)#, result_type = 'popular')
	            if not new_tweets:
        	        print("No more tweets found")
                	break
	            for tweet in new_tweets:
        	        f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                	        '\n')
	            tweetCount += len(new_tweets)
        	    print("Downloaded {0} tweets".format(tweetCount))
	            max_id = new_tweets[-1].id
        	except tweepy.TweepError as e:
	            # Just exit if any error
        	    print("some error : " + str(e))
	            break

	print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
	tweetArr[x] = tweetCount


from yahoo_finance import Share
Twitter = Share('TSLA')
print Twitter.get_price()
Twitter.refresh()
print Twitter.get_price()
print Twitter.get_days_range()

from pprint import pprint
pprint(Twitter.get_historical('2017-03-15', '2017-03-22'))

Closes = [li['Close'] for li in Twitter.get_historical('2016-09-20', '2016-09-27')]
print Closes

years = [2012, 2013, 2014, 2015, 2016,2017]

plt.figure(1)
plt.title('Daily Closing Stock Price')
plt.xlabel('Day')
plt.ylabel('Closing Price ($)')
plt.subplot(211)
plt.plot_date(years, Closes, 'ro', None, True, False)
#plt.tight_layout

plt.subplot(212)
plt.plot(years, tweetArr, 'ro')


plt.show()
