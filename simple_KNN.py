import os
import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

os.chdir('/gpfs/scratch/kar6058/Interviews')
file_name = "iris.data"
data =  pd.read_csv(file_name, sep=",")
titles =["petal_length", "petal_width", "sepal_length", "sepal_width", "flower_type"]
data.columns = titles
y = data["flower_type"]
X = data[data.columns.drop("flower_type")]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scores_list = []

for k in range(1, 26):
    KNN = KNeighborsClassifier(n_neighbors=k)
    KNN.fit(X_train, y_train)
    y_pred = KNN.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(range(1, 26), scores_list)
plt.xlabel("k")
plt.ylabel("Testing Accuracy")