import os
import csv

os.system("python GetTweets.py")
os.system("python ExtractStockPrices.py")

with open('stock.csv', 'r') as csv:
	content = csv.readlines()
content = [x.strip() for x in content]
content = [x.split(",") for x in content]
stockDay= []
stockPrice = []
for y in content:
	stockDay.append(y[0])
	stockPrice.append(y[1])
print (stockDay)
print (stockPrice)


with open('data.csv', 'r') as csv2:
	newcont = csv2.readlines()
newcont = [n.strip() for n in newcont]
newcont = [n.split(",") for n in newcont]
tweetDay= []
tweetPrice = []
for z in newcont:
	tweetDay.append(z[0])
	tweetPrice.append(z[1])
print (tweetDay)
print (tweetPrice)

