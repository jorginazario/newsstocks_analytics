import os
import csv
import matplotlib.pyplot as plt

os.system("python GetTweets.py")
os.system("python ExtractStockPrices.py")

with open('stock.csv', 'r') as csv:
	content = csv.readlines()
content = [x.strip() for x in content]
content = [x.split(",") for x in content]
stockDay= []
stockPrice = []
for y in reversed(content):
	stockDay.append(y[0])
	stockPrice.append(y[1])
print (stockDay)
print (stockPrice)


with open('data.csv', 'r') as csv2:
	newcont = csv2.readlines()
newcont = [n.strip() for n in newcont]
newcont = [n.split(",") for n in newcont]
tempTweetDay= []
tempTweetNum = []
for z in newcont:
	tempTweetDay.append(z[0])
	tempTweetNum.append(z[1])
print (tempTweetDay)
print (tempTweetNum)

#NEED TO REDUCE TWEETDAYLIST AND TWEETLIST
tweetNum = []
counter=0
looper=0
for l in tempTweetDay:
	if l == stockDay[counter]:
		tweetNum.append(tempTweetNum[looper])
		if counter < len(stockDay)-1:
			counter = counter+1
	looper = looper+1

print (tweetNum)

#PLOTTING
plt.figure(1)
plt.subplot(211)

plt.title('Tweets on Company per Day')
plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.grid(True)
plt.bar(range(len(tweetNum)), tweetNum, 0.5, color='blue')
plt.tight_layout()


plt.figure(1)
plt.subplot(212)
plt.title('Closeing Stock Price per Day')
plt.xlabel('Date')
plt.ylabel('Closing Stock price($)')
plt.grid(True)
plt.plot(range(len(stockPrice)), stockPrice, 'g')
plt.tight_layout()
plt.show()
