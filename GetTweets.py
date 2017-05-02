# This program retrieves the number of mentions of a company in twitter for
# each day over the past week. The number of mentions per day are saved in data.txt file.

#LIBRARIES
import tweepy
from datetime import timedelta, date
import datetime as DT
import sys
import jsonpickle
import os
import csv
import time

maxTweets = 1000000                                   # Some arbitrary large number
tweetsPerQry = 100                                    # this is the max number of tweets the twitter API permits to retrieve per query

API_KEY = 'rF1UhAhVJsmie822K1bXN5lvd'                 # To access the twitter API
API_SECRET = 'UykH43jgHn5SWYHTprLyfrQPWKl7V2ODu2MhJVTqIJosjbLn5a'
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):                                         # When credentials dont match
    print ("Can't Authenticate")
    sys.exit(-1)

searchQuery = '#'                                     # hHshtag we are searching for
searchQuery += raw_input("Please enter the hashtag you want to search for: ")

day = int(time.strftime("%d"))                        # Today's date
month = int(time.strftime("%m"))                      # Today's date
year = int(time.strftime("%Y"))                       # Today's date
end_date = date(year, month, day+1)                   # Date range we are searching for
start_date = end_date- DT.timedelta(days=8)
delta = timedelta(days=1)                             # To jump to next day in our date range

from_date = start_date                                # First day
to_date = from_date + delta
with open('data.csv', 'w') as saveFile:               # data.csv file is where the number of tweets per day will be saved
	while to_date <= end_date:                        # Loop to navigate through the week to search for the number of tweets per day
		tweetCount = 0                                # To keep track of the number of tweets
		sinceId = None                                # If results from a specific ID onwards are required, set since_id to that ID.
		max_id = -1L                                  # If results below a specific ID are required, set max_id to that ID.
		print("Downloading max {0} tweets".format(maxTweets))
		while tweetCount < maxTweets:
			try:
				if (max_id <= 0):
					if (not sinceId):
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since=from_date , until=to_date) # searches for the hashtag entered using the twitter API with the specified parameters
					else:
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId, since=from_date , until=to_date)
				else:
					if (not sinceId):
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since=from_date , until=to_date)
					else:
						new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId, since=from_date , until=to_date)

				if not new_tweets:
					print("No more tweets found")
					break

				tweetCount += len(new_tweets)          # Count the number of tweets found for the previous search and add them to the total count for the day
				print ("Downloaded {0} tweets".format(tweetCount))
				max_id = new_tweets[-1].id             # Set max_id to lowest max_id from previous search. This means the search starts with the oldest tweet for the day
                                                       # and loops until it finds the newest tweet for each day

			except tweepy.TweepError as e:
				print("Some error : " + str(e))
				break

		print("There were: ", tweetCount, " tweets for ", from_date.strftime("%Y-%m-%d"))
		writer = csv.writer(saveFile, delimiter = ',')  # Save the number of tweets found for the day in data.csv file
		writer.writerows([[from_date.strftime("%Y-%m-%d"), str(tweetCount)]])

		to_date += delta                                # Loop through next date
		from_date += delta

saveFile.close()
print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, "data.csv"))
