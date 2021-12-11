# Pandas is used for data manipulation
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import csv


# Read in data and display first 5 rows
train_features = pd.read_csv('csv_files/dataTrain.csv', header = None)
test_features = pd.read_csv('csv_files/dataTest.csv', header = None)

# print(features.head(5))

# One-hot encode the data using pandas get_dummies
train_features = pd.get_dummies(train_features)
# Display the first 5 rows of the last 12 columns
# features.iloc[:,5:].head(5)

# Use numpy to convert to arrays
import numpy as np

# Labels are the values we want to predict
# labels = np.array(features['actual'])
labels = np.array(train_features.iloc[:,5])
ids = np.array(test_features.iloc[:-1,0])

# print(labels)


# Remove the labels from the features
# axis 1 refers to the columns
test_features = test_features.drop(test_features.columns[5], axis = 1)
train_features = train_features.drop(train_features.columns[5], axis = 1)

# print(features)

# Saving feature names for later use
# feature_list = list(features.columns)

# Convert to numpy array
train_features = np.array(train_features)
test_features = np.array(test_features)

# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
# train_features, test_features, train_labels, test_labels = train_test_split(
#     features, labels, test_size = 0.20
# )

# The baseline predictions are the historical averages
# baseline_preds = test_features[:, feature_list.index('average')]

# Baseline errors, and display average baseline error
# baseline_errors = abs(baseline_preds - test_labels)
# print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier


# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

# Train the model on training data
rf.fit(train_features, labels)

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
print(predictions)
# exit(0)

# Calculate the absolute errors
# errors = abs(predictions - test_labels)

# Print out the mean absolute error (mae)
# print('Mean Absolute Error:', round(np.mean(errors), 10), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
# mape = 100 * (errors / test_labels)
# print(mape)
# print(np.mean(mape))
# print("predictions:")
# print(predictions)
# print("test_labels:")
# print(test_labels)
# print("errors:")
# print(errors)
# print("mape:")
# print(mape)
# print("np.mean(mape):")
# print(np.mean(mape))

# Calculate and display accuracy
# accuracy = 100 - np.mean(errors * 100)

# for i in range(len(predictions)):
#     if predictions[i] < 0:
#         predictions[i] = -1
#     else:
#         predictions[i] = 1

# print("Confusion Matrix: ",
#     confusion_matrix(test_labels, predictions))
      
# print ("Accuracy : ",
#     accuracy_score(test_labels, predictions)*100)
      
# print("Report : ",
#     classification_report(test_labels, predictions))

# from sklearn.metrics import roc_curve, auc, roc_auc_score

# false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, predictions)
# print(auc(false_positive_rate, true_positive_rate))
# print(roc_auc_score(test_labels, predictions))

# print('Accuracy:', round(accuracy, 2), '%.')

print(test_features[0])
result = []
for i in range(len(predictions)):
    pred = predictions[i]
    pred += 1
    pred /= 2
    pred = 1 - pred
    pred = round(pred, 2)
    result.append([int(test_features[i][0]), pred])

print(result)

f = open('predictionsTest.csv', 'a')
writer = csv.writer(f)
writer.writerow(['Id', 'Predicted'])
for i in range(len(predictions)):
    writer.writerow(result[i])

