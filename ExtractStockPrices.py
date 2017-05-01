#!/usr/bin/python

from yahoo_finance import Share
import csv
from datetime import timedelta, date
import datetime as DT
import time

companylist = open('NASDAQ.csv')
NASDAQ = csv.reader(companylist)
NamesWithTags = dict()
for row in NASDAQ:
	if row[1] in NamesWithTags:
		continue
	else:
		NamesWithTags[row[1]] = row[0]

companylist = open('NYSE.csv')
NYSE = csv.reader(companylist)
for row in NYSE:
	if row[1] in NamesWithTags:
		continue
	else:
		NamesWithTags[row[1]] = row[0]

companylist = open('AMEX.csv')
AMEX = csv.reader(companylist)
for row in AMEX:
	if row[1] in NamesWithTags:
		continue
	else:
		NamesWithTags[row[1]] = row[0]

Company = raw_input("Please enter the formal name of a company, for example enter\n\nBarnes & Noble, Inc.\n\ninstead of\n\nBarnes & Noble\n:")
try:
	Stock = Share(NamesWithTags[Company])
except KeyError:
	Tag = raw_input(Company + " isn't the formal name of any company we have stored. However if you know " + Company + "'s stock tag you can enter it here (or enter -1 to quit): ")
	if Tag == "-1":
		exit(0)
	NamesWithTags[Company] = Tag
	Stock = Share(NamesWithTags[Company])

print (time.strftime("%Y-%m-%d")) #Todays date
day = int(time.strftime("%d"))
month = int(time.strftime("%m"))
year = int(time.strftime("%Y"))
end_date = date(year, month, day+1)
start_date = end_date- DT.timedelta(days=7)

#stockDict = Stock.get_historical

WeekPrices = [li['Close'] for li in Stock.get_historical(str(start_date), str(end_date))]
print WeekPrices
stockDict =  Stock.get_historical(str(start_date), str(end_date))

with open('stock.csv', 'w') as saveFile:
	for i in range(len(stockDict)):
		writer = csv.writer(saveFile, delimiter = ',')
		writer.writerows([[stockDict[i]["Date"], stockDict[i]["Close"]]])

saveFile.close()
