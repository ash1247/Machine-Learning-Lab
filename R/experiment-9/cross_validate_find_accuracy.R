library(e1071)
library(caret)
library(RWeka)

capabilities( )["tcktk"] 
require( tcltk )  

data <- read.csv(tk_choose.files(), header = TRUE)
kfolds <- createFolds(data$buysComputer, k=5)
sum = 0

for (i in kfolds) {
	train <- data[-i,]
	test <- data[i,]
	model <- OneR(buysComputer~., data=train)
	prediction <- predict(model, test)
	cfMatrix <- confusionMatrix(data=prediction, test$buysComputer)
	sum <- sum + cfMatrix$overall[1]
}

accuracy <- sum / length(kfolds)
accuracy