import plotly.plotly as py
from plotly.graph_objs import *

d = {}
m =  
counter  = 1

with open('data.txt','r') as f:
	for line in f:
		date,mentions= line.split(":")
		d["date" + str(counter)] = date
		m["mentions" + str(counter)] = mentions
		counter = counter + 1
			
			

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.iplot(data, filename = 'basic-line')
