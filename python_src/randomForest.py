# Pandas is used for data manipulation
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import sys
import csv
import os
from os.path import exists
import matplotlib.pyplot as plt


to_csv = False
if len(sys.argv) != 2:
    print("Usage: python randomForest.py <train|csv>")
    exit(1)
else:
    if sys.argv[1] == "train":
        filename = "csv_files/dataTrain.cv"
    elif sys.argv[1] == "csv":
        to_csv = True
        filename = "csv_files/dataTest.cv"
    else:
        print("Incorrect argument ", sys.argv[1], ", use train or csv")

# Pandas is used for data manipulation
import pandas as pd

# Read in data and display first 5 rows
train_features = pd.read_csv('csv_files/dataTrain.csv')
if to_csv: 
    test_features = pd.read_csv('csv_files/dataTest.csv')

# One-hot encode the data using pandas get_dummies
train_features = pd.get_dummies(train_features)
# Display the first 5 rows of the last 12 columns
# features.iloc[:,5:].head(5)

# Use numpy to convert to arrays
import numpy as np

# Labels are the values we want to predict
# labels = np.array(features['actual'])
labels = np.array(train_features.iloc[:,5])

# Remove the labels from the features
# axis 1 refers to the columns
train_features = train_features.drop(train_features.columns[5], axis = 1)
if to_csv: test_features = test_features.drop(test_features.columns[5], axis = 1)

# Convert to numpy array
train_features = np.array(train_features)
if to_csv: test_features = np.array(test_features)


# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
#if not to_csv:
#    train_features, test_features, train_labels, test_labels = train_test_split(
#        train_features, labels, test_size = 0.20
#    )

# The baseline predictions are the historical averages
# baseline_preds = test_features[:, feature_list.index('average')]

# Baseline errors, and display average baseline error
# baseline_errors = abs(baseline_preds - test_labels)
# print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 200, random_state = 42, min_samples_leaf = 1000)
# rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)

# Train the model on training data
predictions = 0
if to_csv:
    rf.fit(train_features, labels)
    predictions = rf.predict(test_features)
#else:
#    rf.fit(train_features, train_labels)

#predictions = rf.predict(test_features)

if not to_csv:
    acc = []
    mape_acc = []
    auc_score = []
    for i in range(20):
        training_features, test_features, train_labels, test_labels = train_test_split(
            train_features, labels, test_size = 0.20
        )
        rf.fit(training_features, train_labels)

        predictions = rf.predict(test_features)

        # Use the forest's predict method on the test data

        # Calculate the absolute errors
        errors = abs(predictions - test_labels)

        # Print out the mean absolute error (mae)
        #print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

        # Calculate mean absolute percentage error (MAPE)
        mape = 100 * (errors / test_labels)

        # Calculate and display accuracy
        accuracy = 100 - np.mean(errors * 100)

        for i in range(len(predictions)):
            if predictions[i] < 0:
                predictions[i] = -1
            else:
                predictions[i] = 1

        #print("Confusion Matrix:\n",
        #    confusion_matrix(test_labels, predictions))
            
        #print ("Accuracy : ",
        #    accuracy_score(test_labels, predictions)*100)

        acc.append(accuracy_score(test_labels, predictions))
            
        #print("Report : ",
        #    classification_report(test_labels, predictions))

        from sklearn.metrics import roc_curve, auc, roc_auc_score

        false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, predictions)
        auc_score.append(auc(false_positive_rate, true_positive_rate))

        #plt.plot(false_positive_rate, true_positive_rate, 'b', label = 'AUC = %0.2f' % auc(false_positive_rate, true_positive_rate))
        #plt.plot([0, 1], [0, 1],'r--')
        #plt.xlim([0, 1])
        #plt.ylim([0, 1])
        #plt.show()
        # Calculate and display accuracy

        accuracy = 100 - abs(np.mean(mape))
        mape_acc.append(accuracy)
        #print('Accuracy:', round(accuracy, 2), '%.')

    print("Accuracy", sum(acc)/len(acc))
    print("Mape Accuracy", sum(mape_acc)/len(mape_acc))
    print("Auc", sum(auc_score)/len(auc_score))

else:
    result = []
    for i in range(len(predictions)):
        pred = predictions[i]
        pred += 1
        pred /= 2
        pred = 1 - pred
        pred = round(pred, 5)
        result.append([int(test_features[i][0]), pred])

    if exists("predictions.csv"):
        print("Removing predictions.csv . . .\n")
        os.remove("predictions.csv") 

    print("Generating predictions.csv . . .\n")
    f = open('predictions.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(['Id', 'Predicted'])
    for i in range(len(predictions)):
        writer.writerow(result[i])