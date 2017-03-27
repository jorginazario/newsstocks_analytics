#!/usr/bin/env python2.7

import matplotlib.pyplot as plt			#needed for graphing
import numpy as np				#numpy creates arrays for data to be graphed



#This uses numpy to create a python array (just one way of formatting data
#t1 = np.arange(0.0, 5., 0.1)			#evenly sampled... takes form (min, max, stepsize)
#t2 = np.arange(0., 5., 0.02)

#syntax for when you manually want to enter in the data
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')		#takes form (x, y, formatting)


#syntax for when using a numpy array with multiple graphys
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3)


#A lack of formatting will create a line which you can adjust the width of (linewidth=2.0)


#sets axis (without it it automatically adjusts to show all points)
#plt.axis([0, 6, 0, 20])

#Dummy data for graphs
years = [2012, 2013, 2014, 2015, 2016, 2017]
pricey = [12.22, 13.23, 18.04, 31.77, 42.46, 35.10]
twittery= [32, 44, 53, 87, 109, 93] 

plt.figure(1)					#the figure(1) command is a default
plt.subplot(211)				#you can create multiple plots on the same figure (notation is #of subplots, figure #, which subplot)
plt.plot(years, pricey, 'g--')
plt.title('Average Stock Price per Year')	#Title of subplot
plt.xlabel('Year')				#X and Y axis titles for first subplot
plt.ylabel('Average Price($)')
#plt.grid(True)					#Can show grid if we so choose

plt.subplot(212)				#this creates the lower subplot
plt.plot(years, twittery, 'ro')
plt.title('Twitter Mentions per Year')
plt.xlabel('Year')
plt.ylabel('# of Twitter mentions(Hundreds)')

#plt.figure(2)					#if we wanted we could create multiple different figures at once 
plt.tight_layout()				#makes sure subplots do not overlap
plt.show()					#this displays the developed figures


