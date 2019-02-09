import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random
import operator
import random
import warnings
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from math import sqrt
from collections import Counter



def k_nearest(data, predict,  n_neighbors):

    if len(data) >= n_neighbors:

        warnings.warn('k is set to a value less than total voting groups.')

    distances = []

    for group in data:

        for features in data[group]:

            e_dist = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([e_dist, group])

    votes = [i[1] for i in sorted(distances)[:n_neighbors]]
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / n_neighbors

    return vote_result,confidence




def classify(dataX, dataY, train, testData, testResults, n_neighbors, usingAllData):
    if usingAllData:
        df = pd.read_csv('featuresForAllPersons2.csv')
    else:
        df = pd.read_csv('featuresForAllPersons.csv')
    df = df.drop(labels='personID', axis=1, inplace=False)
    df = df.replace("jumping",1)
    df = df.replace("walking", 2)
    df = df.replace("standing", 3)
    df = df.replace("running", 4)
    df = df.replace("bike", 5)
    df = df.replace("sitting", 6)
    df = df.replace("stepper", 7)

    full_data = df.astype(float).values.tolist()

    random.shuffle(full_data)

    test_size = 0.10

    if usingAllData:
        train_set = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        test_set = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    else:
        train_set = {1: [], 2: [], 3: []}
        test_set = {1: [], 2: [], 3: []}
    train_data = full_data[:-int(test_size * len(full_data))]
    test_data = full_data[-int(test_size * len(full_data)):]

    for i in train_data:
        train_set[i[0]].append(i[1:])

    for i in test_data:
        test_set[i[0]].append(i[1:])

    correct = 0
    total = 0
    testResults = []
    predicted = []

    for group in test_set:

        for data in test_set[group]:

            vote, confidence = k_nearest(train_set, data, n_neighbors)
            testResults.append(group)
            predicted.append(vote)

            if group == vote:
                correct += 1

            total += 1
    testResults = np.array(testResults)
    predicted = np.array(predicted)
    print('Accuracy = ' + str(round((correct / total), 5)))
    print(confusion_matrix(testResults, predicted))
    print(classification_report(testResults, predicted))
    print("k= ",n_neighbors)

#classify(0,0,0,0,0,10,True)