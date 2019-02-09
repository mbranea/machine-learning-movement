import ownClassifier as ownCJochen
import pandas as pd
import numpy as np
import csv
import ownClassifierByFabian as ownCFabian
import allAlgorithsms as allAlg
from sklearn.model_selection import train_test_split
import random

#TODO   die präsie (Fabian)
#       die eigenen aufgenommmenen Daten mit einfügen (Maxim)
#       die algorithmen trainieren und richtige ergebnisse bekommen (alle)
#       k-neig. zu ende programmieren (Jochen)
#       neue Features einbauen (Maxim)
#       aufteilen der daten in main zum laufen bringen (Jochen)
#       generateFeatures und scaleData in dataProcessing so anpassen, dass die neuen Features ans ende der Datei gesetzt wird und nicht überschreibt (Jochen)

# Die imports sind mir so eingefallen, können aber mehr sein
# In PyCharm war es Strg+Alt+S und dann Project->ProjectInterpreter
# Oder einfach mit Strg+Enter auf den Fehler (schreibe das weil ich es mir selbst nicht merken kann)

def main():
    #print("Hello World")


    prediectDontKnowDataGirl = False
    predictPersonWithNormalActivities = False
    train = True
    neighbors = 10
    test_size = 0.2
    usingAllData = True

    if usingAllData:
        df = pd.read_csv("featuresForAllPersons2.csv")
    else:
        df = pd.read_csv("featuresForAllPersons.csv")

    if train:
        if predictPersonWithNormalActivities:
            X = np.array(df.iloc[1:1600, 2:21])
            y = np.array(df.iloc[1:1600, 1:2])
        else:
            X = np.array(df.iloc[:, 2:21])
            y = np.array(df.iloc[:, 1:2])


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

        #print(X_train)
        allAlg.useAllClassifier(X_train, y_train, train, X_test, y_test, neighbors, usingAllData)

        ownCJochen.classify(X_train, y_train, train, X_test, y_test, neighbors, usingAllData)
        print("Done: ownAlgorithmJochen")

        df.columns = [0] * len(df.columns)
        X = df.iloc[:, 1:21]

        train, test = train_test_split(X, test_size=test_size, random_state=0)
        ownCFabian.classify(train, test, neighbors)

    else:
        if prediectDontKnowDataGirl:
            df = pd.read_csv("featuresForAllPersons3.csv")
            X = np.array(df.iloc[:, 2:21])
        else:
            X = np.array(df.iloc[1621:1800, 2:21])

        #print(X)
        allAlg.decision_trees(0, 0, False, X, 0)

main()
