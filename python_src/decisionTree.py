import csv
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import sklearn.tree as tree
  

# Function importing Dataset
def importdata():
    train_data = pd.read_csv(
        'dataPrep.csv',
        sep= ',', header = None)

    test_data = pd.read_csv(
        'dataPrepTest.csv',
        sep= ',', header = None)
      
    # Printing the dataswet shape
    print ("Dataset Length: ", len(train_data))
    print ("Dataset Shape: ", train_data.shape)
      
    # Printing the dataset obseravtions
    print ("Dataset: ",train_data.head())

    return train_data, test_data

def getfinaldata(balance_data, test_data):
    X_train = np.c_[balance_data.values[:, 0:5], balance_data.values[:, 6:8], balance_data.values[:, 9:26], balance_data.values[:, 28:44]]
    X_train = pd.DataFrame(X_train)
    Y_train = balance_data.values[:, 5]
    Y_train = pd.DataFrame(Y_train)
    X_test = np.c_[test_data.values[:, 0:5], test_data.values[:, 6:8], test_data.values[:, 9:26], test_data.values[:, 28:44]]
    X_test = pd.DataFrame(X_test)

    Y_train[0] = Y_train[0].astype('category')

    return X_train, Y_train, X_test
  
# Function to split the dataset
def splitdataset(balance_data):
    # Separating the target variable
    # X = np.c_[balance_data.values[:, 0:5], balance_data.values[:, 6:8], balance_data.values[:, 9:26], balance_data.values[:, 28:44]]
    X = np.c_[balance_data.values[:, 0:5], balance_data.values[:, 6:]]

    X = pd.DataFrame(X)
    Y = balance_data.values[:, 5]
    Y = pd.DataFrame(Y)


    Y[0] = Y[0].astype('category')

    """
    X[0] = X[0].astype('int')
    X[1] = X[1].astype('int')
    X[2] = X[2].astype('int')
    X[3] = X[3].astype('int')
    X[4] = X[4].astype('int')
    X[5] = X[5].astype('int')
    X[6] = X[6].astype('int')
    X[7] = X[7].astype('category')
    X[8] = X[8].astype('int')
    X[9] = X[9].astype('int')
    X[10] = X[10].astype('float64')
    X[11] = X[11].astype('int')
    X[12] = X[12].astype('float64')
    X[13] = X[13].astype('float64')
    X[14] = X[14].astype('float64')
    X[15] = X[15].astype('float64')
    X[16] = X[16].astype('float64')
    X[17] = X[17].astype('float64')
    X[18] = X[18].astype('int')
    X[19] = X[19].astype('int')
    X[20] = X[20].astype('int')
    X[21] = X[21].astype('int')
    X[22] = X[22].astype('int')
    X[23] = X[23].astype('int')
    X[24] = X[24].astype('int')
    X[25] = X[25].astype('category')
    X[26] = X[26].astype('category')
    X[27] = X[27].astype('int')
    X[28] = X[28].astype('int')
    X[29] = X[29].astype('int')
    X[30] = X[30].astype('int')
    X[31] = X[31].astype('int')
    X[32] = X[32].astype('int')
    X[33] = X[33].astype('int')
    X[34] = X[34].astype('int')
    X[35] = X[35].astype('int')
    X[36] = X[36].astype('int')
    X[37] = X[37].astype('int')
    X[38] = X[38].astype('int')
    X[39] = X[39].astype('int')
    X[40] = X[40].astype('int')
    X[41] = X[41].astype('int')
    X[42] = X[42].astype('int')
    """

    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.2)
      
    return X, Y, X_train, X_test, y_train, y_test
      
# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
  
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
  
    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini
      
# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
  
# Function to make predictions
def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))
  

      
# Building Phase
data, test_data = importdata()


X_train, y_train, X_test = getfinaldata(data, test_data)
# X, Y, X_train, X_test, y_train, y_test = splitdataset(data)

clf_gini = train_using_gini(X_train, X_test, y_train)
clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
      
# Operational Phase
print("Results Using Gini Index:")
      
# Prediction using gini
y_pred_gini = prediction(X_test, clf_gini)
# cal_accuracy(y_test, y_pred_gini)
      
print("Results Using Entropy:")
# Prediction using entropy
y_pred_entropy = prediction(X_test, clf_entropy)
# cal_accuracy(y_test, y_pred_entropy)

predic = clf_entropy.predict_proba(X_test)

result = []
for i in range(len(X_test)):
    result.append([int(X_test[0][i]), round(predic[i][0], 2)])

print(result)

f = open('result.csv', 'a')
writer = csv.writer(f)
writer.writerow(['Id', 'Predicted'])
for i in range(len(predic)):
    writer.writerow(result[i])

print(tree.export_text(clf_entropy))
