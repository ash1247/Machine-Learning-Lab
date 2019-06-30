library(caret)
library(e1071)

# Special GUI library for Linux file manager
capabilities( )["tcktk"] 
require( tcltk )  

# Prompts for train data
train <- read.csv(tk_choose.files())
# Prompts for test data
test <- read.csv(tk_choose.files())
# Creates a model based on train data using svmRadial
classification <- train(buysComputer~.,data=train, method="svmRadial")
# Uses that model to predict test data
pre1 <- predict(classification, test)
# Outputs predicted value
pre1