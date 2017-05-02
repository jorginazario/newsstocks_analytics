import os
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime

os.system("python GetTweets.py")			#runs code that handles twitter API (saves to csv file)
os.system("python ExtractStockPrices.py")		#runs code that handles yahoo finance API (saves to csv file)

with open('stock.csv', 'r') as csv:			#need to open csv with read capabilities
	content = csv.readlines()
content = [x.strip() for x in content]			#strip and split the lines from the csv file
content = [x.split(",") for x in content]		#each line is of the form <date>,<closing stock price>
stockDay= []						#initialize lists
stockPrice = []
for y in reversed(content):				#need to reverse the content because yahoo finance API returns is backwards
	stockDay.append(y[0])				#daylist gets first element
	stockPrice.append(y[1])				#pricelist gets second element

with open('data.csv', 'r') as csv2:			#similar to the getting of the info from the stock prices csv
	newcont = csv2.readlines()
newcont = [n.strip() for n in newcont]
newcont = [n.split(",") for n in newcont]
tempTweetDay= []
tempTweetNum = []
for z in newcont:
	tempTweetDay.append(z[0])
	tempTweetNum.append(z[1])

#The yahoo finance api only returns values for days that are not weekends (whereas twitter does all days in the date range) 
#so for the graph we use the stockDays (recieved from the yahoo finance API) and need to separate out only the tweet Values from the dates
#that we have stock prices for

#NEED TO REDUCE TWEETDAYLIST AND TWEETLIST
tweetNum = []						#new list of corresponding tweets
counter=0
looper=0
for l in tempTweetDay:
	if l == stockDay[counter]:			#if the days in each of the csv files are the same
		tweetNum.append(tempTweetNum[looper])	#append the tweet number to the new (shorter) list
		if counter < len(stockDay)-1:		#the looper loops through the longer list (updates each time)
			counter = counter+1		#and the counter goes through the shorter list (only updates when match found)
	looper = looper+1


#PLOTTING
plt.figure(1)						#chose to plot one full figure and two subplots
plt.subplot(211)

plt.title('Tweets on Company per Day')
plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.grid(True)
plt.bar(xrange(len(tweetNum)), tweetNum, 0.5, color='blue')	#can't plot dates (need to plot ints) so plots x-axis as a range
plt.xticks(xrange(len(tweetNum)), stockDay, size='small')	#then writes over the x ticks with the dates list
plt.tight_layout()						#helps with formatting the two subplots


plt.figure(1)
plt.subplot(212)
plt.title('Closeing Stock Price per Day')
plt.xlabel('Date')
plt.ylabel('Closing Stock price($)')
plt.grid(True)
plt.plot(xrange(len(stockPrice)), stockPrice, 'g')
plt.xticks(xrange(len(stockPrice)), stockDay, size='small')
plt.tight_layout()
plt.show()							#need to show to have a visible graph pop up

exit()
