import simplejson as json
import calendar
import datetime
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
import collections

def analyzeTimeStamp(filename):
	listOfHours = []
	with open(filename, "r") as txtfile:
		for line in txtfile:
			if line.startswith('2'):
				timeline = line.split(" ")[1]
				listOfHours.append(timeline.split(":")[0])
				#print timeline.split(":")[0]
	return listOfHours

listOfHours = analyzeTimeStamp("localdb_test.txt")

hourCounter = {}
for hour in listOfHours:
	if hour in hourCounter:
 		hourCounter[hour]+=1
	else:
		hourCounter[hour] = 1

for key,value in hourCounter.iteritems():
	print key, ":", value

# def getDayOfWeek(filename):
# 	dateList = []
# 	with open(filename, "r") as txtfile:
# 		for line in txtfile:
# 			if line.startswith('2'):
# 				dateLine = line.split(" ")[0]
# 				#print date.split(" ")[0]
# 				dateSplit = dateLine.split("-")
# 				dateList.append(dateSplit)
# 	return dateList

class countHolder:
	def __init__(self, name, dayList):
		self.name = name
		self.dayList = dayList

	def printCounter(self):
		for indexDay, day in enumerate(self.dayList):
			for indexHour, hour in enumerate(day):
				if self.dayList[indexDay][indexHour] != 0:
					print "Currently", indexDay, "at", indexHour, "is equal to", self.dayList[indexDay][indexHour]

def formatLine(line):
	day = line.split(" ")[0]
	day = day.split("-")
	time = line.split(' ')[1]
	time = int(time.split(':')[0])
	day = datetime.date(int(day[0]), int(day[1]), int(day[2]))
	return datetime.datetime.weekday(day), time

def initializeList():
	listvar = []
	for i in range(7):
		listvar.append([])
		for j in range(24):
			listvar[i].append(0)
	return listvar

# def readFromFile(filename):
# 	placeName = ''
# 	dayList = initializeList()
# 	listOfPlaceObjects = []
# 	with open(filename, 'r') as txt:
# 		for line in txt:
# 			if line.startswith('%'):
# 				placeName = line.strip()
# 	 			placeName = placeName.replace('%', '')
# 	 		elif line.startswith('*****'):
# 	 			newPlace = countHolder(placeName, dayList)
# 	 			listOfPlaceObjects.append(newPlace)
# 	 			dayList = initializeList()
# 	 		else:
# 	 			#dayList[0][0] = 0 first 0 represents day of the week, second 0 represents hour and what it equals to is the counter
# 	 			day, hour = formatLine(line)
# 	 			dayList[day][hour] += 1
# 	return listOfPlaceObjects

totalList = []

# listOfObjects = readFromFile("localdb_test.txt")
# for objectt in listOfObjects:
# 	print objectt.name
# 	if objectt.name == "theponybarues":
# 		pony = objectt
# 	objectt.printCounter()
# 	totalList.append(np.array(objectt.dayList))

# for x in pony.dayList:
# 	for y in x:
# 		ponyCount.append(pony.dayList[x][y])

# for indexDay, day in enumerate(pony.dayList):
# 	for indexHour, hour in enumerate(day):
# 		tempList = []
# 		tempList.append(pony.dayList[indexDay][indexHour])
# 		ponyY.append(tempList)
# 		# ponyY.append(pony.dayList[indexDay][indexHour])

# ponyYnp = np.array(ponyY)
# ponyXnp = np.array(ponyX)



# totalNumpy = np.array(totalList)
# print totalNumpy

# lista = initializeList()
# for entry in lista:
# 	print len(entry)

def readFromFile(filename):
	placeName = ''
	tweetList = []
	locList = []
	with open(filename, 'r') as txt:
		for line in txt:
			if line.startswith('%'):
				placeName = line.strip()
				placeName = placeName.replace('%', '')
				placeDict = collections.defaultdict()
				placeDict['name'] = placeName
				placeDict['tweets'] = {}
			elif line.startswith('*****'):
				locList.append(placeDict)
			else:
				day, hour = formatLine(line)
				if day in placeDict['tweets'].keys() == True:
					print "reached day"
					if hour in placeDict['tweets'][day].keys() == True:
						placeDict['tweets'][day][hour] += 1
					else:
						placeDict['tweets'][day][hour] = 1
				else:
					dayDict = {hour: 1}
					placeDict['tweets'][day] = dayDict
	return locList

placeDict = readFromFile('hotels')
print placeDict

# dayList = getDayOfWeek("localdb_test.txt")

# dayOfWeek = []
# for day in dayList:
# 	print day
# 	d = datetime.date(int(day[0]), int(day[1]), int(day[2]))
# 	print datetime.datetime.weekday(d) #prints day of the week. 0 is monday. 6 is sunday.

# locations = [()]
# print locations