#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np




from yahoo_finance import Share
Twitter = Share('AAPL')
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
#plt.subplot(211)
plt.plot_date(years, Closes, 'ro', None, True, False)
#plt.tight_layout
plt.show()
