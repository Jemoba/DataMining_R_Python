AUTHOR : Jessica Bailey

CLASS : CSC 333 Program Language Theory

PROJECT : Write a program that takes two data files that contain the sequence, step size, ordered pair, 
	and data in each line,
and find the sum for each line of data.  After find the average of the 
	data for each set based on matching step size and ordered 
pair. Continue by finding the differences
	of the averages between the two data files.  Then plot these differences using a heatmap.


LANGUAGES : Python/R



REQUIREMENTS : 	Python 2.7 / R
	
		WINDOWS/MAC OSX		   
		Data files must be located in the same directory




HOW TO(MAC OSX):
Navigate to the main file (DataMining_Preprocessing.py) in the terminal.  
		Run the main file using "python 
DataMining_Preprocessing.py".  Once completed the USER will 
		be prompted to input the name of the first data file, including
	the extension(This will be 
		the data file that gets subtracted from).  USER will complete file input.  Once program has 
		completed
	program will open a pdf file of the newly created heatmap for USER to view.

HOW TO(WINDOWS):Navigate to the main file(DataMining_Preprocessing.py) in the command prompt.  Run the main 
		file using "DataMining_Preprocessing.py".  Once completed the USER will be prompted to input
		the name of the first data file, including the extension(This will be the data file that gets
		subtracted from).  USER will complete file input.  Once program has completed execution of 
		python program files, USER will be prompted to navigate to and select the file for heatmap 
		creation(Processed_Data.txt).  Once USER selects open, the program will then continue execution
		of the R program within the command prompt and the program will then automatically open the pdf
		file of the heatmap for the USER to view.	


NOTES :
	User can go into directory to view the file information that was used to create the heatmap (Processed_Data.txt)

	If program does not open pdf heatmap, it will be located in the same directory (RPlots.pdf[MAC OSX]) or 
		(RPlot.pdf[WINDOWS])
 
	When running the large data sets provided the program completes in about 1 hour

	There are provided smaller samples included. (file1.txt, file2.txt, test1.txt, test2.txt)

	There are provided correct outputs for each smaller sample files included (fileset_info.txt, testset_info.txt)	
	Also included is the Processed_Data.txt file from completion of the large data trans_POS and trans_NEG (trans_data.txt)

TROUBLESHOOTING: Under WINDOWS the USER may need to change the execution path in command prompt to allow for R to
			run properly.  This can be done using the path (C:\Program Files\R\R-3.3.2\bin) or (C:\Program
			Files\R\R-3.3.2\bin\x64).  To find more information on changing paths go to http://www.computer
			hope.com/issues/ch000549.htm .
		Under MAC OSX there are no known issues so far