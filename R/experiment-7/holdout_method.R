library(RWeka)
library(caret)
library(klaR)
library(e1071)

capabilities( )["tcktk"] 
require( tcltk )  

#this program uses RWeka and caret
#Holdout method

train <- read.csv(tk_choose.files(), header = TRUE)
test <- read.csv(tk_choose.files(), header = TRUE)
model <- OneR(class~., data=train)
prediction <- predict(model, test)
cfMatrix <- confusionMatrix(data = prediction, test$class)
cfMatrix

