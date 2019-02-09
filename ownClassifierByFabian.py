from sklearn.metrics import classification_report, confusion_matrix
import math
import numpy as np
import operator

def euclideanDistance(instance1, instance2):
    distance = 0
    #print("instance1:",instance1)
    #print("instance2:",instance2)
    for i in range(0, len(instance1)):
        distance += pow((float(instance1[i]) - float(instance2[i+1])), 2)

    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    train = np.array(trainingSet)
    #print(train)
    for row in train:
        #print("row:",row)
        dist = euclideanDistance(testInstance, row)
        distances.append((row, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        #print(distances[x][0])
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][0]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][0] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

def classify(trainData, testData, n_neighbors):
    #trainData = np.array(trainData).tolist()
    #testData = np.array(testData).tolist()
    #print(trainData)
    #print(trainData)
    #print(testData)

    predictions = []
    test = []
    label = []
    #print("testData:",testData)
    label = np.array(testData.iloc[:, 0:1])
    test = np.array(testData.iloc[:, 1:20])
    for row in test:
        #print("row:", row)
        neighbors = getNeighbors(trainData, row, n_neighbors)
        result = getResponse(neighbors)
        predictions.append(result)
        #print(result)
    #print('> predicted=' + repr(result) + ', actual=' + repr(row[0]))
    accuracy = getAccuracy(label, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    print(confusion_matrix(label, predictions))
    print(classification_report(label, predictions))
    print("done OwnClassifierFabian, k = ", n_neighbors)
    return 0

