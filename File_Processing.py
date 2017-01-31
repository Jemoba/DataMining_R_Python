#Jessica Bailey
#
#
#Works on files where the data set has spaces between each number
#If files have data all together (no spaces), then remove the colons(:) from the process file at [3:]

import os
import sys
import File_Data as data
import Difference as dif
import Average as avg
import Vector_Sums as sum


#Checks file given by user to insure file exists
def checkFile(input, num):
	if os.path.exists(input):
		processFile(input, num)
	else:
		print "Invalid file path."
		filename = raw_input("Please enter a valid file name.")
		checkFile(filename, num)

#Parses each file into the required types of data				
def processFile(input, num):
        print "Processing file " + str(num) + "..."
        file = open(input, "r")
        #Section for parsing first input file
        #Writes data to new files for use in the program later
        if num == 1:
                stepfile = open("StepsOne.txt", 'w')
                pairfile = open("PairsOne.txt", 'w')
                datafile = open("DataOne.txt", 'w')
                for line in file:
                        oneData = line.split(" ")
                        stepfile.write(str(oneData[1])+"\n")
                        pairfile.write(str(oneData[2])+"\n")
                        datafile.write(str(oneData[3:])+"\n")
                        del oneData
                stepfile.close()
                pairfile.close()
                datafile.close()
                file.close()
        #Section for parsing the second input file
        #Writes data to new files for use in the program later
        elif num == 2:
                stepfile = open("StepsTwo.txt", 'w')
                pairfile = open("PairsTwo.txt", 'w')
                datafile = open("DataTwo.txt", 'w')
                for line in file:
                        twoData = line.split(" ")
                        stepfile.write(str(twoData[1])+"\n")
                        pairfile.write(str(twoData[2])+"\n")
                        datafile.write(str(twoData[3:])+"\n")
                        del twoData
                stepfile.close()
                pairfile.close()
                datafile.close()
                file.close()
        else:
                print "File number not valid..."
        print "File " + str(num) + " processed successfully."
        if num == 2:
                sum.sumVectors()

	
