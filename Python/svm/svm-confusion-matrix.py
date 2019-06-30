import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy
from sklearn.svm import SVC  

# Set a random seed form weight matrices.
numpy.random.seed(2)

# Read training and test dataset.
train = pd.read_csv('./holdout_train.csv')
test = pd.read_csv('./holdout_test.csv')

# LabelEncoder to convert categorical to numeric value.
number = LabelEncoder()

# Convert categorical values to numeric.
for i in train:
    train[i] = number.fit_transform(train[i].astype('str'))

# Split input and output columns; x = input columns, y = output columns.
x_train = train.iloc[:, :-1]
y_train = train.iloc[:, -1]

# Do the same for test dataset.
for i in test:
    test[i] = number.fit_transform(test[i].astype('str'))

x_test = test.iloc[:, :-1]
y_test = test.iloc[:, -1]

svclassifier = SVC(kernel='linear')  
svclassifier.fit(x_train, y_train)  

# Do a prediction on 4-tuple test dataset.
predictions = svclassifier.predict(x_test)  

# Build confusion matrix
cfm = confusion_matrix(y_test, predictions)
# Calc accuracy
acc = accuracy_score(y_test, predictions)

# Print acc and cfm
print('Accuracy:', acc)
print('Prediction  No  Yes')
print('        No  {}   {}'.format(cfm[0][0], cfm[0][1]))
print('       Yes  {}   {}'.format(cfm[1][0], cfm[1][1]))
