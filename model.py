from data_preprocess import *
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#train 80%, test 20%
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size = 0.2, random_state = 7)

list_lon = [index[0] for index in x_train]
list_lat = [index[1] for index in x_train]
list_lon_test = [index[0] for index in x_test]
list_lat_test = [index[1] for index in x_test]
min_lon = min(list_lon)
max_lon = max(list_lon)

min_lat = min(list_lat)
max_lat = max(list_lat)
grid_size = 0

#--------------------------------------------------------------------------------------------------------------------------------#

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC 
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def get_data(gridSize):
    creatGrid(min_lon, max_lon, min_lat, max_lat, gridSize)
    findGrid(x_train, y_train, x_test, y_test)

def model(clf,p):
    correct = 0 
    allPredict = 0
    for x_key, y_key in zip(dict_xTest, dict_yTest):
        if(x_key in dict_xTrain.keys() and y_key in dict_yTrain.keys()):
            if clf=="knn":
                if(p <= len(dict_xTrain[x_key])):
                    model = KNeighborsClassifier(p)
                    X = dict_xTrain[x_key]
                    y = dict_yTrain[y_key]

            if clf == 'dct':
                model = DecisionTreeClassifier(criterion=p)
                X = dict_xTrain[x_key]
                y = dict_yTrain[y_key]

            if clf == 'svm':
                if(len(set(dict_yTrain[y_key])) > 1):
                    model = SVC()
                    X = dict_xTrain[x_key]
                    y = dict_yTrain[y_key]
            
            if clf == 'gpc':
                model = GaussianNB()
                X = dict_xTrain[x_key]
                y = dict_yTrain[y_key]

            if clf == 'mlp':
                model = MLPClassifier()
                X = dict_xTrain[x_key]
                y = dict_yTrain[y_key]

            model.fit(X, y)
            predict_ = model.predict(dict_xTest[x_key])
            allPredict += len(predict_)
            correct += accuracy_score(dict_yTest[y_key], predict_, normalize=False)
    return (correct/allPredict)*100

def create_dict(grid_size):
    creatGrid(min_lon, max_lon, min_lat, max_lat, grid_size)
    findGrid(x_train, y_train, x_test, y_test)