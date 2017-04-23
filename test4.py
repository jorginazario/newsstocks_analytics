#Tweepy
import tweepy
from datetime import timedelta, date
import sys
import jsonpickle
import os

maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.
fName2 = 'data.txt'
# Replace the API_KEY and API_SECRET with your application's key and secret.
API_KEY = 'rF1UhAhVJsmie822K1bXN5lvd'
API_SECRET = 'UykH43jgHn5SWYHTprLyfrQPWKl7V2ODu2MhJVTqIJosjbLn5a'
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

searchQuery = '#' # this is what we're searching for
searchQuery += raw_input("Please enter the company name you want to search for: ")

# Enter the date range
print "Enter today's date"
day_string = raw_input("Day (dd): ")
day = int(day_string)
month_string = raw_input("Month (mm): ")
month = int(month_string)
year_string = raw_input("Year (yyyy): ")
year = int(year_string)
end_date = date(year, month, day+1)
start_date = date(year, month, day-7)

delta = timedelta(days=1)
from_date = start_date
to_date = from_date + delta

with open(fName, 'w') as f:
	saveFile = open ('data.txt', 'w')
	while to_date <= end_date:
		print from_date.strftime("%Y-%m-%d")
		print to_date.strftime("%Y-%m-%d")
		# If results from a specific ID onwards are reqd, set since_id to that ID.
		# else default to no lower limit, go as far back as API allows
		sinceId = None
		# If results only below a specific ID are, set max_id to that ID.
		# else default to no upper limit, start from the most recent tweet matching the search query.
		max_id = -1L
		tweetCount = 0
		print("Downloading max {0} tweets".format(maxTweets))
		while tweetCount < maxTweets:
			try:
				if (max_id <= 0):
					if (not sinceId):
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since=from_date , until=to_date)#, result_type = 'popular')
					else:
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId, since=from_date , until=to_date)#, result_type = 'popular'
				else:
					if (not sinceId):
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since=from_date , until=to_date)#, result_type = 'popular')
					else:
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId, since=from_date , until=to_date)#, result_type = 'popular')

				if not new_tweets:
					print("No more tweets found")
					break

				for tweet in new_tweets:
					f.write(jsonpickle.encode(tweet.created_at, unpicklable=False) + ': ' + jsonpickle.encode(tweet.text, unpicklable=False) + '\n')

				tweetCount += len(new_tweets)
				print ("Downloaded {0} tweets".format(tweetCount))
				max_id = new_tweets[-1].id

			except tweepy.TweepError as e:
				# Just exit if any error
				print("some error : " + str(e))
				break

		print("There were: ", tweetCount, " tweets for ", from_date.strftime("%Y-%m-%d"))
		saveFile.write(from_date.strftime("%Y-%m-%d") + ': ' + str(tweetCount) + '\n')

		to_date += delta
		from_date += delta

saveFile.close()
print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
