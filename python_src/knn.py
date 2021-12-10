# Begin by importing all necessary libraries
import pandas as pd
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import sklearn.model_selection as model_selection
from sklearn.svm import SVC

data = pd.read_csv('iris.csv')
    
# It is a good idea to check and make sure the data is loaded as expected.
# print(data.head(5))

data.drop('Id', axis=1, inplace=True)

# Pandas ".iloc" expects row_indexer, column_indexer  
X = data.iloc[:,:-1].values
# Now let's tell the dataframe which column we want for the target/labels.  
y = data['Species']

# Test size specifies how much of the data you want to set aside for the testing set. 
# Random_state parameter is just a random seed we can use.
# You can use it if you'd like to reproduce these specific results.
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.20, random_state=27)

print(X_train)  
print(y_train)

SVC_model = SVC()
# KNN model requires you to specify n_neighbors,
# the number of points the classifier will look at to determine what class a new point belongs to
KNN_model = KNeighborsClassifier(n_neighbors=5)

SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

# Accuracy score is the simplest way to evaluate
print("SVC accuracy: ", accuracy_score(SVC_prediction, y_test))
print("KNN accuracy: ", accuracy_score(KNN_prediction, y_test))
# But Confusion Matrix and Classification Report give more details about performance
print(confusion_matrix(SVC_prediction, y_test))
print(classification_report(KNN_prediction, y_test))