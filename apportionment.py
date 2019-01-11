###############
#	reps.py
#	Proportionally distribute reps given:
#	Total Population per State
#	Max Total Reps
###############

import csv
import math

maxReps = 435
totalReps = 0
datafile = 'data2010.csv'

def numconv(x):
	return float(x)

# Defines new priority
def calcvalue(n, p):
	return p*math.sqrt(n/(n+2))

#Sort by priority value
def resort(input):
	return input.sort(key=lambda x: float(x[1]), reverse=True)

# Init Data
f = open("log.txt", "a+")
g = open("result.txt", "a+")
datafile = open(datafile, 'r')
datareader = csv.reader(datafile, delimiter=',')
data = []
for row in datareader:
    data.append(row)

# Transform population to first priority value
for entry in data:
	entry[1] = calcvalue(float(entry[2]), float(entry[1]))
	totalReps += float(entry[2])
	entry[2] = numconv(entry[2])
	
#Initialize sort of data
resort(data)

while totalReps < maxReps:
	totalReps+=1
	data[0][1] = calcvalue(float(data[0][2]), float(data[0][1]))
	data[0][2]+=1
	f.write("["+str(totalReps)+"],"+data[0][0]+"," +str(data[0][1])+","+str(data[0][2])+"\r\n")
	resort(data)
	

data.sort(key=lambda x: float(x[2]), reverse=True)
#g.write(str(data)) 
print data
	

	#[x][y][z]
	# x = state
	# y = pop/priortiy
	# z = reps