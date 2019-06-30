import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy
from keras.models import Sequential
from keras.layers import Dense

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

# Create a sequential ANN model.
model = Sequential()
# Add first layer; neurons = 10, inputs = 4.
model.add(Dense(10, input_dim=4, activation='relu'))

# Add second layer; neurons = 4.
model.add(Dense(4, activation='relu'))

# Add output layer; 1 neron for output 0 or 1.
model.add(Dense(1, activation='sigmoid'))
# Compile this model.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Now train-up the model, iterations = 150, batch = 10.
model.fit(x_train, y_train, epochs=150, batch_size=10)

# Do a prediction on 4-tuple test dataset.
predictions = model.predict(x_test)
predicted = [int(round(x[0])) for x in predictions]

# Build confusion matrix
cfm = confusion_matrix(y_test, predicted)
# Calc accuracy
acc = accuracy_score(y_test, predicted)

# Print acc and cfm
print('Accuracy:', acc)
print('Prediction  No  Yes')
print('        No  {}   {}'.format(cfm[0][0], cfm[0][1]))
print('       Yes  {}   {}'.format(cfm[1][0], cfm[1][1]))
