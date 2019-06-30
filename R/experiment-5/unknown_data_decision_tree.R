library(RWeka)
library(caret)
library(e1071)

capabilities( )["tcktk"] 
require( tcltk )  

data <- read.csv(tk_choose.files())
test <- read.csv(tk_choose.files())
classification <- naiveBayes(buysComputer~.,data=data)
pre1 <- predict(classification, test, type="class")
pre1