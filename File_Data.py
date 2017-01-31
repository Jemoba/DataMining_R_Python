#Jessica Bailey
#Holds all file data for the two files
#

file1 = []
file2 = []
avgOne = []
avgTwo = []
diffList = []
diffOut = []

def setFile1(step, pair, sum):
	list = [step, pair, sum]
	file1.append(list)
	del step, pair, sum
	
def setFile2(step, pair, sum):
	list = [step, pair, sum]
	file2.append(list)
	del step, pair, sum
	
def setAvgOne(step, pair, sum, count):
	sum = sum/count
	list = (step, pair, sum)
	avgOne.append(list)
	del step, pair, sum, count
	
def setAvgTwo(step, pair, sum, count):
	sum = sum/count
	list = (step, pair, sum)
	avgTwo.append(list)
	del step, pair, sum, count
	
def setDiff(pair, step, diff):
	list = (step, pair, diff)
	diffList.append(list)
	
def setDiffOut(input):
	diffOut.append(input)
	
def getFile1():
	return file1
	
def getFile2():
	return file2

def getAvgOne():
	return avgOne
	
def getAvgTwo():
	return avgTwo
	
def getDiffList():
	return diffList
	
def getDiffOut():
	return diffOut
