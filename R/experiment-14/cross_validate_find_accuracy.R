library(e1071)
library(caret)
library(nnet)

# Special GUI library for Linux file manager
capabilities( )["tcktk"] 
require( tcltk )  

# Read data
data <- read.csv(tk_choose.files(), header = TRUE)
# create k folds of data 
kfolds <- createFolds(data$buysComputer, k=2)
sum = 0

for (i in kfolds) {
	# data is divided from -i index into train data
	train <- data[-i,]
	# data is divided from i index into train data
	test <- data[i,]
	# trains a model from train data using nnet
	model <- train(buysComputer~., data=train, method="nnet")
	# predicts the test data from the trained model
	prediction <- predict(model, test)
	# creates a cfMatrix from predicted data and class values
	cfMatrix <- confusionMatrix(data=prediction, test$buysComputer)
	# adds cfMatrix$overall[1] value which contains the accuracy value
	# to variable sum
	sum <- sum + cfMatrix$overall[1]
}
# finds the accuracy from sum and length of kfolds
accuracy <- sum / length(kfolds)
# prints accuracy
accuracy