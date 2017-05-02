#!/usr/bin/python

from yahoo_finance import Share
import csv
from datetime import timedelta, date
import datetime as DT
import time

companylist = open('NASDAQ.csv')				# Opens the NASDAQ.csv file
NASDAQ = csv.reader(companylist)				# Allows the file to be read as cells
NamesWithTags = dict()							# Declares a dictionary that stores company names and stock tags
for row in NASDAQ:								# Reads the file row by row
	if row[1] in NamesWithTags:					# Checks if the first entry in the row is already in the dictionary
		continue
	else:
		NamesWithTags[row[1]] = row[0]			# Adds a company's name as a key to the dictionary with its stock tag as the value

companylist = open('NYSE.csv')					# Opens the NYSE.csv file
NYSE = csv.reader(companylist)					# Allows the file to be read as cells
for row in NYSE:								# Reads the file row by row
	if row[1] in NamesWithTags:					# Checks if the first entry in the row is already in the dictionary
		continue
	else:
		NamesWithTags[row[1]] = row[0]			# Adds a company's name as a key to the dictionary with its stock tag as the value

companylist = open('AMEX.csv')					# Opens the AMEX.csv file
AMEX = csv.reader(companylist)					# Allows the file to be read as cells
for row in AMEX:								# Reads the file row by row
	if row[1] in NamesWithTags:					# Checks if the first entry in the row is already in the dictionary
		continue
	else:
		NamesWithTags[row[1]] = row[0]			# Adds a company's name as a key to the dictionary with its stock tag as the value

Company = raw_input("Please enter the formal name of a company, for example enter\n\nBarnes & Noble, Inc.\n\ninstead of\n\nBarnes & Noble\n:")
try:
	Stock = Share(NamesWithTags[Company])		# Checks that the company the user entered is in the dictionary and if so assigns Stock the value of the company's stock tag
except KeyError:
	Tag = raw_input(Company + " isn't the formal name of any company we have stored. However if you know " + Company + "'s stock tag you can enter it here (or enter -1 to quit): ")							# If the company the user entered isn't in the dictionary then the user is prompted to enter the stock tag themself or enter -1 to quit
	if Tag == "-1":
		exit(0)
	NamesWithTags[Company] = Tag				# Adds the user entered tag to the dictionary
	Stock = Share(NamesWithTags[Company])		# Sets stock equal to the stock tag of the company entered

day = int(time.strftime("%d"))					# Gets the current day
month = int(time.strftime("%m"))				# Gets the current month
year = int(time.strftime("%Y"))					# Gets the current year
end_date = date(year, month, day)				# Sets the end_date as the current date
start_date = end_date- DT.timedelta(days=7)		# Sets the start_date as 7 days before the end_date


WeekPrices = [li['Close'] for li in Stock.get_historical(str(start_date), str(end_date))]
print WeekPrices
stockDict =  Stock.get_historical(str(start_date), str(end_date))		# Gets the stock data in the given date range

with open('stock.csv', 'w') as saveFile:								# Opens a csv file to save the output in
	for i in range(len(stockDict)):										# Loops through each dictionary in the list
		writer = csv.writer(saveFile, delimiter = ',')					# Writes in a csv format with a comma as the dilemeter between cells
		writer.writerows([[stockDict[i]["Date"], stockDict[i]["Close"]]])	# Saves the date of a stock price as the first cell in a row and the closing price as the second cell

saveFile.close()														# Closes the save file
