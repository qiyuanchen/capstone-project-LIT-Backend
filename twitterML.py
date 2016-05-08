import simplejson as json
import calendar
import datetime

def analyzeTimeStamp(filename):
	listOfHours = []
	with open(filename, "r") as txtfile:
		for line in txtfile:
			timeline = line.split(" ")[1]
			listOfHours.append(timeline.split(":")[0])
			print timeline.split(":")[0]
	return listOfHours

listOfHours = analyzeTimeStamp("localdb.txt")

hourCounter = {}
for hour in listOfHours:
	if hour in hourCounter:
 		hourCounter[hour]+=1
	else:
		hourCounter[hour] = 1

for key,value in hourCounter.iteritems():
	print key, ":", value

def getDayOfWeek(filename):
	dateList = []
	with open(filename, "r") as txtfile:
		for line in txtfile:
			dateLine = line.split(" ")[0]
			#print date.split(" ")[0]
			dateSplit = dateLine.split("-")
			dateList.append(dateSplit)
	return dateList

dayList = getDayOfWeek("localdb.txt")

for day in dayList:
	print day
	d = datetime.date(int(day[0]), int(day[1]), int(day[2]))
	print datetime.datetime.weekday(d) #prints day of the week. 0 is monday. 6 is sunday.

#for loop to navigate through text file
#read each line and record the hour when the tweet was posted
#counter for each hour
#dictionary to count the time stamps