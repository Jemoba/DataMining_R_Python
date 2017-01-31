#Jessica Bailey
#
#The difference function will find the difference between the data in the two files sets.
#
import os
import File_Data as data
import gc

#Sets up the out file of processed data
def setupFile():
        pair = []
        step = []
        avg = []
        i = 0
        j = 1
        for line in data.getDiffList():
                pair.append(line[0])
                step.append(line[1])
                avg.append(line[2])
        stepCount = len(set(data.getDiffList()))
        while(i < stepCount):
                newline = "["+str(pair[i])+"] "+str(avg[i])
                while (j < stepCount):
                        if pair[i] == pair[j]:
                                newline += " "+str(avg[j])
                                pair.pop(j)
                                avg.pop(j)
                                stepCount = len(pair)
                        else:
                                j += 1
                data.setDiffOut(newline)
                i += 1
                j = i + 1

#Finds the differences between the two files
def difference():
        print "Finding differences between data 1 and data 2..."
        count = 0
        for a in data.getAvgOne():
                for b in data.getAvgTwo():
                        if a[0] == b[0] and a[1] == b[1]:
                                newsum = a[2] - b[2]
                                count += 1
                                data.setDiff(a[1], a[0], newsum)
        i = 0
        j = 1
        print "Differences found."
        stepCount = len(set(data.getDiffList()))
        print "Setting up matrix file..."
        setupFile()
        print "Matrix file complete."
        print "Creating out file..."
        gc.collect()
        fileOut()

#Writes the output file of Processed Data	
def fileOut():
        file = open("Processed_Data.txt", "w")
        file.write("Rows ")
        stepfile = open("StepsOne.txt", 'r')
        steps = []
        for line in stepfile:
                steps.append(line)
        sort = set(steps)
        new = []
        for item in sort:
                new.append(int(item))
        for line in sorted(new):
                file.write("S_"+str(line)+" ")
        file.write("\n")
        for line in data.getDiffOut():
                file.write(line+"\n")
                del line
        print "Out file created"
