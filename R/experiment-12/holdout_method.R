library(caret)
library(nnet)

# Special GUI library for Linux file manager
capabilities( )["tcktk"] 
require( tcltk )  

# Holdout method

# Prompts for train data
train <- read.csv(tk_choose.files(), header = TRUE)
# Prompts for test data
test <- read.csv(tk_choose.files(), header = TRUE)
# Creates a model from train data using method nnet
model <- train(class~., data=train, method="nnet")
# Makes a prediction about the test data
prediction <- predict(model, test)
# Creates a confusion matrix based on the predicted data
cfMatrix <- confusionMatrix(data = prediction, test$class)
# Prints cfMatrix
cfMatrix

