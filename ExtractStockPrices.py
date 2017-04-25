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
WeekPrices = [li['Close'] for li in Stock.get_historical('2017-4-15', '2017-4-22')]
print WeekPrices
