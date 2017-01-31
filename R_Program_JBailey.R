#Jessica Bailey
#R Script that opens the processed_data file and turns the data into a heatmap
#

#Used to clean up the user visuals
suppressPackageStartupMessages(library(gplots))
#Library required to utilize heatmap.2
library(gplots)
#Used to check what type of system the program is running on
system <- .Platform$OS.type
#tryCatch Block used to create and open the heatmap on a Windows based system
if (system == "windows"){
  tryCatch({
    #Next four lines find the path to the needed file for openning
    path <- file.choose()
    open <- normalizePath(dirname(path))
    open_path <- file.path(open, "Processed_Data.txt")
    file <- read.csv(open_path,sep = " ")
    #finds the number of columns in the file
    num <- max(count.fields(open_path, sep = " "))
    num <- num - 1
    row.names(file) <- file$Rows
    file <- file[,2:num]
    file_matrix <- data.matrix(file)
    col = c("dark blue","blue", "dark green", "green","red","orange", "yellow",  "white")
    pdf('RPlot.pdf', width = 24, height = 24)
    heatmap.2(file_matrix,main = 'Processed Data', key=T, density.info="none", col= col,dendrogram="none",trace="none", cexRow = 1.5, cexCol = 1.5, margins = c(4,4))
    message("Heatmap creation successful!")
    tryCatch({
      #Section to open the heatmap pdf for the user to view
      pdf_path <- file.path(open, "RPlot.pdf")
      system2('open', args = pdf_path, wait = FALSE)
    },
    error = function(err){
      #Used for error catching
      message("Error openning heatmap pdf file. The heatmap can be viewed from the program directory.")
    })
  },
    error = function(err){
      #Used for error catching
      message(paste("MY_ERROR: ",err))
      message("Error has occured with heatmap creation.")
  })
}
#tryCatch Block used to create and open the heatmap on a Unix based system(MAC OSX)
if (system == "unix"){
  tryCatch({
    #Next four lines find the path to the needed file for openning
    path <- file.choose()
    open <- normalizePath(dirname(path))
    open_file <- file.path(open, "Processed_Data.txt")
    file <- read.csv(open_file, sep = " ")
    #finds the number of columns in the file
    num <- max(count.fields(open_file, sep = " "))
    num <- num - 1
    row.names(file) <- file$Rows
    file <- file[,2:num]
    file_matrix <- data.matrix(file)
    col = c("dark blue","blue", "dark green", "green","red","orange", "yellow",  "white")
    pdf('RPlot.pdf', width = 24, height = 24)
    file <- heatmap.2(file_matrix,main = 'Processed Data', key=T, density.info="none", col= col,dendrogram="none",trace="none", cexRow = 1.5, cexCol = 1.5, margins = c(4,4))
    message("Heatmap creation successful!")
    tryCatch({
      #Section to open the heatmap pdf for user view
      pdf_path <- file.path(open, "RPlot.pdf")
      system2('open', args = pdf_path, wait = FALSE)
    },
    error = function(err){
      #Used for error catching
      message("Error openning heatmap pdf file. The heatmap can be viewed from the program directory.")
    })
  },
  error = function(err){
    #Used for error catching
    message(paste("MY_ERROR: ",err))
    message("Error has occured with heatmap creation.")
  })
}