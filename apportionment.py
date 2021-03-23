###############
#	apportionment.py
#	Proportionally distribute reps given:
#	Total Population per State
#	Max Total Reps
###############

import csv
import math

maxReps = 435
totalReps = 0
datafile = 'data/data2010_edit.csv'

def numconv(x):
	return float(x)

# Defines new priority
def calcvalue(n, p):
	return p*math.sqrt(n/(n+2))
	
def calcfirst(p):
	return p/math.sqrt(2)

#Sort by priority value
def resort(input):
	return input.sort(key=lambda x: float(x[1]), reverse=True)

# Init Data
f = open("data/log.txt", "w+")
g = open("data/result.txt", "w+")
datafile = open(datafile, 'r')
datareader = csv.reader(datafile, delimiter=',')
data = []
for row in datareader:
    data.append(row)

# Transform population to first priority value
for entry in data:
	entry[1] = calcfirst(float(entry[1]))
	totalReps += float(entry[2])
	entry[2] = numconv(entry[2])
	
#Initialize sort of data
resort(data)

while totalReps < maxReps:
	totalReps+=1
	f.write("["+str(totalReps)+"],"+data[0][0]+"," +str(data[0][1])+","+str(data[0][2]+1)+"\r\n")
	data[0][1] = calcvalue(float(data[0][2]), float(data[0][1]))
	data[0][2]+=1
	
	resort(data)
	

data.sort(key=lambda x: float(x[2]), reverse=True)
for entry in data:
	g.write(entry[0]+"\t\t"+str(entry[2])+"\r\n")
print "Done."
	

	#[x][y][z]
	# x = state
	# y = pop/priortiy
	# z = reps
