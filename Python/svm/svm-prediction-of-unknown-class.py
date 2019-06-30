import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy
from sklearn.svm import SVC  

# Set a random seed form weight matrices.
numpy.random.seed(7)

# Read training and test dataset.
train = pd.read_csv('./unknown_train.csv')
test = pd.read_csv('./unknown_test.csv')

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

x_test = test.iloc[:]

svclassifier = SVC(kernel='linear')  
svclassifier.fit(x_train, y_train)  

# Do a prediction on unknown dataset.
predictions = svclassifier.predict(x_test)  

# Result of the predictions.
outputs = predictions

# Print the predicted results.
for i in outputs:
    print('Prediction: Yes') if i == 1 else print('Prediction: No')

