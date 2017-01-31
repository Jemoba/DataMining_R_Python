#Jessica Bailey
#
#main file
#

import subprocess as sub
import File_Processing as pro
import time
import os
import platform

#Function used to remove files used by program
def deleteFiles():
        os.remove("DataOne.txt")
        os.remove("DataTwo.txt")
        os.remove("StepsOne.txt")
        os.remove("StepsTwo.txt")
        os.remove("PairsOne.txt")
        os.remove("PairsTwo.txt")


#Takes user input files and checks that they are valid
filename1 = raw_input("Please enter the file name for the first data file: ")
filename2 = raw_input("Please enter the file name for the second data file: ")
start_time = time.clock()
pro.checkFile(filename1, 1)
pro.checkFile(filename2, 2)
end_time = time.clock()
#Used to find time the program took to execute
total_time = (end_time - start_time)/60
#Used to find what system the user is running on
system = platform.system()
print "Time to execute: ", total_time, " minutes"
deleteFiles()
print "Executing heatmap creation..."
#Section used to call R Script if user is on MAC OSX
if system == "Darwin":
        try:
                sub.call(["Rscript --vanilla r_program_jbailey.r"], shell=True)
        except name:
                print "An error occured at " + name + "."
#Section used to call R Script if user is on WINDOWS
elif system == "win32" or system == "Windows":
        try:
                sub.call( 'Rscript --vanilla  r_program_jbailey.r', shell = True)
        except:
                print "An error occured."
else:
		#Message displayed to user if an error occurs in calling the R Script
        print "System cannot call R_Program Data for heatmap creation..."
	
