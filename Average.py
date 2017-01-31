#Jessica Bailey
#avgSums will find the average of the sums of vectors that correspond to each sequence and step sizes
#

import Difference as dif
import File_Data as data
import time
import copy

#Function to find the Averages of the first file
def findAvg1():
        i = 0
        j = 1
        step = []
        pair = []
        sum = []
        for line in data.getFile1():
                step.append(line[0])
                pair.append(line[1])
                sum.append(line[2])
        length1 = len(pair)
        while (i < length1 - 1):
                avg = 0
                avg += sum[i]
                count = 1.0
                while (j < length1):
                        if pair[i] == pair[j] and step[i] == step[j]:
                                count += 1
                                avg += sum[j]
                                pair.pop(j)
                                step.pop(j)
                                sum.pop(j)
                                length1 = len(pair)
                        else:
                                j += 1
                data.setAvgOne(pair[i], step[i], avg, count)
                i += 1
                j = i + 1
        del step, pair, sum, i, j, length1

#Function to find the Averages of the second file	
def findAvg2():
	i = 0
	j = 1
	step = []
	pair = []
	sum = []
	for line in data.getFile2():
		step.append(line[0])
		pair.append(line[1])
		sum.append(line[2])
	length1 = len(pair)
	while (i < length1 - 1):
		avg = 0
		avg += sum[i]
		count = 1.0
		while (j < length1):
			if pair[i] == pair[j] and step[i] == step[j]:
				count += 1
				avg += sum[j]
				pair.pop(j)
				step.pop(j)
				sum.pop(j)
				length1 = len(pair)
			else:
				j += 1
		data.setAvgTwo(pair[i], step[i], avg, count)
		i += 1
		j = i + 1
	del step, pair, sum, i, j, length1

#Function to call the Average functions, display update information to user and call the next python file function
def avgSums():
	start_time2 = time.clock()
	print "Finding average of data set 1."
	findAvg1()
	print "Data set 1 find average successful."
	end_time2 = time.clock()
	time2 = str((end_time2 - start_time2) / 60)
	print "Time for avg 1: " + time2 + " minutes."
	start_time1 = time.clock()
	print "Finding average of data set 2."
	findAvg2()	
	print "Data set 2 find average successful."
	end_time1 = time.clock()
	time1 = str((end_time1 - start_time1) / 60)
	print "Time for avg 2: " + time1 + " minutes."
	dif.difference()

	
