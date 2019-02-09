import numpy as np
import pandas as pd

initial = "isolatedData"
activities =["jumping","standing","walking"]
activities2 = ["jumping", "standing", "walking", "running", "bike", "sitting", "stepper"]
testPersons = ["p1","p2","p3","p4","p5","p6","p7","p8"]
categories = ["AccX","AccY","AccZ","GyroX","GyroY","GyroZ","MagX","MagY","MagZ"]

def buildPathsForPerson(person):
    paths = []
    for i in range(len(activities)):
        for n in range(1,60):
            nr=str(n)
            if(n<10):
                nr="0"+str(n)
            #path = initial + "\\" +activities[i]+ "\\" +testPersons[person] + "\\" + "s" + nr + "RL.csv"
            path = initial + "\\" + activities2[i] + "\\" + testPersons[person] + "\\" + "s" + nr + "RL.csv"
            paths.append(path)
            #path = initial + "\\" + activities[i] + "\\" + testPersons[person] + "\\" + "s" + nr + "LL.csv"
            path = initial + "\\" + activities2[i] + "\\" + testPersons[person] + "\\" + "s" + nr + "LL.csv"
            paths.append(path)

    return paths


def readIntoLine(sourceColumn):
    line = ""
    for i in range(0,125):
        line += str(sourceColumn[i])+","

    return line

def CSVToLine(path):
    dataFile = pd.read_csv(path)
    columnsList = []
    columnsList.append( dataFile.AccX)
    columnsList.append(dataFile.AccX)
    columnsList.append( dataFile.AccX)

    columnsList.append( dataFile.GyroX)
    columnsList.append( dataFile.GyroY)
    columnsList.append( dataFile.GyroZ)

    columnsList.append( dataFile.MagX)
    columnsList.append( dataFile.MagY)
    columnsList.append( dataFile.MagZ)

    # = {acc_X,acc_Y,acc_Z,gyro_X,gyro_Y,gyro_Z,mag_X,mag_Y,mag_Z}
    line = ""

    lineArray = [readIntoLine(column) for column in columnsList]
    line = line.join(lineArray)
    line  = line[:-1]
    sepLine = line.split(",")

    return sepLine



def read_data(path):

    if "RL.csv" in path:
        dataRL = CSVToLine(path)

        dataRLString=",".join(dataRL)
        return dataRLString+"\n"
    if "LL.csv" in path:
        dataLL = CSVToLine(path)

        dataLLString=",".join(dataLL)

        return dataLLString+"\n"


def loadDataForPerson(person):
    data = ""
    paths = buildPathsForPerson(person)
    for path in paths:
        newData = read_data(path)
        data += newData

    print(data)
    return data
