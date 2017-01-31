#Jessica Bailey
#
#sumVectors will find the sum of the vector in each line of data within the files
#

import Difference as dif
import Average as avg
import Vector_Sums as sum
import File_Data as data


def sumVectors():
        #Section for finding the sums of the first file
        sums = []
        print "Summing vectors in files"
        datafile = open("DataOne.txt", 'r')
        for a in datafile:
                total1 = 0
                for num1 in a:
                        if num1 == '1' or num1 == "1\n":
                                total1 += 1
                sums.append(total1)
        pair = []
        pairfile = open("PairsOne.txt", 'r')
        for line in pairfile:
                pair.append(line.rstrip('\n'))
        step = []
        file = open("StepsOne.txt", 'r')
        for line in file:
                step.append(line.rstrip('\n'))
        i = 0
        #Creates a list that contains the steps, pairs, and sums found
        while i < len(pair):
                data.setFile1(step[i], pair[i], sums[i])
                i += 1
        #Section for finding the sums of the second file
        datafile = open("DataTwo.txt", 'r')
        sums2 = []
        for b in datafile:
                total2 = 0
                for num2 in b:
                        if num2 == '1' or num2 == "1\n":
                                total2 += 1
                sums2.append(total2)
        pair = []
        pairfile = open("PairsTwo.txt", 'r')
        for line in pairfile:
                pair.append(line.rstrip('\n'))
        step = []
        file = open("StepsTwo.txt", 'r')
        for line in file:
                step.append(line.rstrip('\n'))
        i = 0
        #Creates a list that contains the steps, pairs, and sums found
        while (i < len(pair)):
                data.setFile2(step[i], pair[i], sums2[i])
                i += 1
        print "Vectors summed successfully."
        #Calls the next file to find the averages of the data in each files
        avg.avgSums()
