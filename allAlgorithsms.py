import ownClassifier as ownC
import numpy as np
import pickle as pickle
from sklearn.neural_network import MLPClassifier
from sklearn import linear_model
from sklearn import svm
from sklearn import neighbors
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cluster import KMeans as kmeans

def cluster(dataX):
    [idx, C] = kmeans(dataX, 7)

def useAllClassifier(dataX, dataY, train, testData, testResults, n_neighbors, usingAllData):
    neural_network(dataX, dataY, train, testData, testResults, usingAllData)
    print("Done: neural_network")
    #bayesian(dataX, dataY, train, testData, testResults)
    #print("Done: bayesian")
    support_vector_machines(dataX, dataY, train, testData, testResults)
    print("Done: support_vector_machines")
    k_nearest_neighbours(dataX, dataY, train, testData, testResults, n_neighbors)
    print("Done: k_nearest_neighbours")
    #k_nearest_neighbours(dataX, dataY, train, testData, testResults, 5)
    #print("Done: k_nearest_neighbours")
    #k_nearest_neighbours(dataX, dataY, train, testData, testResults, 30)
    #print("Done: k_nearest_neighbours")
    stochastic_gradient_descent(dataX, dataY, train, testData, testResults)
    print("Done: stochastic_gradient_descent")
    decision_trees(dataX, dataY, train, testData, testResults)
    print("Done: decision_trees")


def neural_network(dataX, dataY, train, testData, testResults, usingAllData):
    filename = "neural_network_clf"
    if(train):
        dataY2 = dataY
        dataY = []
        for i in dataY2:
            if not usingAllData:
                if i == "jumping":
                    dataY.append([0,0,1])
                elif i == "walking":
                    dataY.append([0, 1, 0])
                elif i == "standing":
                    dataY.append([1, 0, 0])
                else:
                    print("ein Fehler ist aufgetreten")
                    return
            else:
                if i == "jumping":
                    dataY.append([1, 0, 0, 0, 0, 0, 0])
                elif i == "walking":
                    dataY.append([0, 1, 0, 0, 0, 0, 0])
                elif i == "standing":
                    dataY.append([0, 0, 1, 0, 0, 0, 0])
                elif i == "running":
                    dataY.append([0, 0, 0, 1, 0, 0, 0])
                elif i == "bike":
                    dataY.append([0, 0, 0, 0, 1, 0, 0])
                elif i == "sitting":
                    dataY.append([0, 0, 0, 0, 0, 1, 0])
                elif i == "stepper":
                    dataY.append([0, 0, 0, 0, 0, 0, 1])
                else:
                    print("ein Fehler ist aufgetreten")
                    return
            #print(dataX)
        clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False,
              epsilon=1e-08, hidden_layer_sizes=(15,),
              learning_rate='constant', learning_rate_init=0.001,
              max_iter=200, momentum=0.9, n_iter_no_change=10,
              nesterovs_momentum=True, power_t=0.5,  random_state=1,
              shuffle=True, solver='lbfgs', tol=0.0001,
              validation_fraction=0.1, verbose=False, warm_start=False)
        clf.fit(dataX, dataY)
        pickle.dump(clf, open(filename, 'wb'))
    else:
        clf = pickle.load(open(filename, 'rb'))
    predicted = clf.predict(testData)
    predicted2 = predicted
    #print(predicted)
    predicted = []
    countNotPredicted = 0
    for i in predicted2:
        if not usingAllData:
            if i[2] == 1:
                predicted.append("jumping")
            elif i[1] == 1:
                predicted.append("walking")
            elif i[0] == 1:
                predicted.append("standing")
            else:
                predicted.append("Error")
                countNotPredicted += 1
        else:
            if i[0] == 1:
                predicted.append("jumping")
            elif i[1] == 1:
                predicted.append("walking")
            elif i[2] == 1:
                predicted.append("standing")
            elif i[3] == 1:
                predicted.append("running")
            elif i[4] == 1:
                predicted.append("bike")
            elif i[5] == 1:
                predicted.append("sitting")
            elif i[6] == 1:
                predicted.append("stepper")
            else:
                predicted.append("Error")
                countNotPredicted += 1
    print("\n\n")
    print("countNotPredicted:", countNotPredicted)
    if train:
        print("\n\n")
        print(confusion_matrix(testResults, predicted))
        print(classification_report(testResults, predicted))
    else:
        print(predicted)

def bayesian(dataX, dataY, train, testData, testResults):
    filename = "bayesian_reg"
    if (train):
        clf = linear_model.BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
                      fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
                      normalize=False, tol=0.001, verbose=False)
        clf.fit(dataX, dataY)
        pickle.dump(clf, open(filename, 'wb'))
    else:
        clf = pickle.load(open(filename, 'rb'))
    predicted = clf.predict(testData)
    if train:
        print("\n\n")
        print(confusion_matrix(testResults, predicted))
        print(classification_report(testResults, predicted))
    else:
        print(predicted)

def support_vector_machines(dataX, dataY, train, testData, testResults):
    filename = "support_vector_machines_clf"
    if (train):
        clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
                decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
                max_iter=-1, probability=False, random_state=None, shrinking=True,
                tol=0.001, verbose=False)
        clf.fit(dataX, dataY)
        pickle.dump(clf, open(filename, 'wb'))
    else:
        clf = pickle.load(open(filename, 'rb'))
    predicted = clf.predict(testData)
    if train:
        print("\n\n")
        print(confusion_matrix(testResults, predicted))
        print(classification_report(testResults, predicted))
    else:
        print(predicted)

def k_nearest_neighbours(dataX, dataY, train, testData, testResults, n_neighbors):
    for weights in ['uniform', 'distance']:
        for alg in ['brute', 'kd_tree', 'ball_tree']:
            filename = "k_nearest_neighbours_" + weights + "_alg_" + alg + "_clf"
            if (train):
                clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights, algorithm=alg)
                clf.fit(dataX, dataY)
                pickle.dump(clf, open(filename, 'wb'))
            else:
                clf = pickle.load(open(filename, 'rb'))
            predicted = clf.predict(testData)
            if train:
                print("\n\n")
                print(confusion_matrix(testResults, predicted))
                print(classification_report(testResults, predicted))
            else:
                print(predicted)
            print(weights," ",alg," k= ",n_neighbors)

def stochastic_gradient_descent(dataX, dataY, train, testData, testResults):
    filename = "stochastic_gradient_descent_clf"
    if (train):
        clf = SGDClassifier(alpha=0.0001, average=False, class_weight=None,
               early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
               l1_ratio=0.15, learning_rate='optimal', loss='hinge', max_iter=5,
               n_iter=None, n_iter_no_change=5, n_jobs=None, penalty='l2',
               power_t=0.5, random_state=None, shuffle=True, tol=None,
               validation_fraction=0.1, verbose=0, warm_start=False)
        clf.fit(dataX, dataY)
        pickle.dump(clf, open(filename, 'wb'))
    else:
        clf = pickle.load(open(filename, 'rb'))
    predicted = clf.predict(testData)
    if train:
        print("\n\n")
        print(confusion_matrix(testResults, predicted))
        print(classification_report(testResults, predicted))
    else:
        print(predicted)

def decision_trees(dataX, dataY, train, testData, testResults):
    filename = "decision_trees_clf"
    if (train):
        clf = tree.DecisionTreeClassifier()
        clf.fit(dataX, dataY)
        pickle.dump(clf, open(filename, 'wb'))
    else:
        clf = pickle.load(open(filename, 'rb'))
    predicted = clf.predict(testData)
    if train:
        print("\n\n")
        print(confusion_matrix(testResults, predicted))
        print(classification_report(testResults, predicted))
    else:
        count = 1
        for i in predicted:
            print(count, i)
            count += 1
