library(caret)
library(e1071)
library(nnet)

# Special GUI library for Linux file manager
capabilities( )["tcktk"] 
require( tcltk )  

# Prompts for train data
train <- read.csv(tk_choose.files())
# Prompts for test data
test <- read.csv(tk_choose.files())
# Creates a model based on train data using nnet
classification <- train(buysComputer~.,data=train, method="nnet")
# Uses that model to predict test data
pre1 <- predict(classification, test)
# Outputs predicted value
pre1