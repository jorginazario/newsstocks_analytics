#!/usr/bin/python

from yahoo_finance import Share
import csv

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

#StartDay = raw_input("Start Day (dd): ")
#StartMonth = raw_input("Start Month (mm): ")
#EndDay = raw_input("End Day (dd): ")
#EndMonth = raw_input("End Month (mm): ")
#Year = raw_input("Current Year (yyyy): ")

stockDict = Stock.get_historical

WeekPrices = [li['Close'] for li in Stock.get_historical('2017-04-20', '2017-04-25')]
print WeekPrices
stockDict =  Stock.get_historical('2017-04-20', '2017-04-25')

with open('stock.csv', 'w') as saveFile:
	for i in range(len(stockDict)):
		writer = csv.writer(saveFile, delimiter = ',')
		writer.writerows([[stockDict[i]["Date"], stockDict[i]["Close"]]])

saveFile.close()
