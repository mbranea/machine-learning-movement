import pandas as pd
import csv
import math
import shutil, stat
import os


# Label:    0 = standing
#           1 = walking
#           2 = jumping

initial = "isolatedData"
target = "scaledAndCenteredData"
target2 = "scaledAndCenteredData2"
target3 = "scaledAndCenteredData3"

activities = ["jumping", "standing", "walking"]
activities2 = ["unbekannt"]
categories = ["AccX", "AccY", "AccZ", "GyroX", "GyroY", "GyroZ", "MagX", "MagY", "MagZ"]

features = ["MovementLeft", "HighjumpLeft", "BothPositiveLeft", "MovementHighLeft", "MengeAnVorzeichenwechselLeft",
            "MovementRight", "HighjumpRight", "BothPositiveRight", "MovementHighRight", "MengeAnVorzeichenwechselRight"]
averageFeatures = ["AvgAccX", "AvgAccY", "AvgAccZ", "AvgGyroX", "AvgGyroY", "AvgGyroZ", "AvgMagX", "AvgMagY", "AvgMagZ"]


def generateFeatures(fromperson, personcount):
    #with open("featuresForAllPersons.csv", "w", newline='') as myfile:
    with open("featuresForAllPersons3.csv", "w", newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["personID"] + ["Label"] + features + averageFeatures)
        #fVtP = pd.read_csv("fixedValuesToPerson.csv")
        fVtP = pd.read_csv("fixedValuesToPerson3.csv")
        for personNumber in range(fromperson, personcount + 1):
            left = True
            #for path in buildPathsForPerson(personNumber, target):
            for path in buildPathsForPerson(personNumber, target3):
                if left:
                    dfLeft = pd.read_csv(path)
                    left = False
                else:
                    left = True
                    dfRight = pd.read_csv(path)
                    for ind, rowF in fVtP.iterrows():
                        if (rowF.person == personNumber):
                            movementLeft = 0
                            highjumpLeft = 0
                            bothPositiveLeft = 0
                            movementHighLeft = 0
                            vorzeichenLeft = 0
                            mengeAnVorzeichenwechselLeft = 0
                            movementRight = 0
                            highjumpRight = 0
                            bothPositiveRight = 0
                            movementHighRight = 0
                            vorzeichenRight = 0
                            mengeAnVorzeichenwechselRight = 0
                            avgAccX = 0
                            avgAccY = 0
                            avgAccZ = 0
                            avgGyroX = 0
                            avgGyroY = 0
                            avgGyroZ = 0
                            avgMagX = 0
                            avgMagY = 0
                            avgMagZ = 0
                            label = "error"
                            if "standing" in path:
                                label = "standing"
                            elif "walking" in path:
                                label = "walking"
                            elif "jumping" in path:
                                label = "jumping"
                            elif "stepper" in path:
                                label = "stepper"
                            elif "bike" in path:
                                label = "bike"
                            elif "running" in path:
                                label = "running"
                            elif "sitting" in path:
                                label = "sitting"
                            for indexLeft, rowLeft in dfLeft.iterrows():
                                for indexRight, rowRight in dfRight.iterrows():
                                    if (indexLeft == indexRight):
                                        movementLeft += math.sqrt(rowLeft.AccY ** 2 + rowLeft.AccZ ** 2)
                                        # if  row.AccX < abs(rowF.MaxAccX) * -0.7 or row.AccX > abs(rowF.MaxAccX) * 0.7:
                                        if rowLeft.AccX > 0.1:
                                            highjumpLeft += 1
                                        if (rowLeft.AccY < 0 and rowLeft.AccZ < 0) or (
                                                rowLeft.AccY > 0 and rowLeft.AccZ > 0):
                                            bothPositiveLeft += 1
                                        if math.sqrt(rowLeft.AccY ** 2 + rowLeft.AccZ ** 2) > 0.7:
                                            movementHighLeft += 1
                                        if vorzeichenLeft == 0 and (rowLeft.AccY + rowLeft.AccZ) < 0:
                                            vorzeichenLeft = -1
                                        elif vorzeichenLeft == 0 and (rowLeft.AccY + rowLeft.AccZ) > 0:
                                            vorzeichenLeft = 1
                                        elif (vorzeichenLeft == -1 and (rowLeft.AccY + rowLeft.AccZ) > 0) or (
                                                vorzeichenLeft == 1 and (rowLeft.AccY + rowLeft.AccZ) < 0):
                                            mengeAnVorzeichenwechselLeft += 1

                                        movementRight += math.sqrt(rowRight.AccY ** 2 + rowRight.AccZ ** 2)
                                        # if  row.AccX < abs(rowF.MaxAccX) * -0.7 or row.AccX > abs(rowF.MaxAccX) * 0.7:
                                        if rowRight.AccX > 0.1:
                                            highjumpRight += 1
                                        if (rowRight.AccY < 0 and rowRight.AccZ < 0) or (
                                                rowRight.AccY > 0 and rowRight.AccZ > 0):
                                            bothPositiveRight += 1
                                        if math.sqrt(rowRight.AccY ** 2 + rowRight.AccZ ** 2) > 0.7:
                                            movementHighRight += 1
                                        if vorzeichenRight == 0 and (rowRight.AccY + rowRight.AccZ) < 0:
                                            vorzeichenRight = -1
                                        elif vorzeichenRight == 0 and (rowRight.AccY + rowRight.AccZ) > 0:
                                            vorzeichenRight = 1
                                        elif (vorzeichenRight == -1 and (rowRight.AccY + rowRight.AccZ) > 0) or (
                                                vorzeichenRight == 1 and (rowRight.AccY + rowRight.AccZ) < 0):
                                            mengeAnVorzeichenwechselRight += 1

                                        avgAccX += rowLeft.AccX + rowRight.AccX
                                        avgAccY += rowLeft.AccY + rowRight.AccY
                                        avgAccZ += rowLeft.AccZ + rowRight.AccZ
                                        avgGyroX += rowLeft.GyroX + rowRight.GyroX
                                        avgGyroY += rowLeft.GyroY + rowRight.GyroY
                                        avgGyroZ += rowLeft.GyroZ + rowRight.GyroZ
                                        avgMagX += rowLeft.MagX + rowRight.MagX
                                        avgMagY += rowLeft.MagY + rowRight.MagY
                                        avgMagZ += rowLeft.MagZ + rowRight.MagZ
                            durch = 250
                            avgAccX /= durch
                            avgAccY /= durch
                            avgAccZ /= durch
                            avgGyroX /= durch
                            avgGyroY /= durch
                            avgGyroZ /= durch
                            avgMagX /= durch
                            avgMagY /= durch
                            avgMagZ /= durch
                            values = [personNumber, label, movementLeft, highjumpLeft, bothPositiveLeft, movementHighLeft,
                                 mengeAnVorzeichenwechselLeft,
                                 movementRight, highjumpRight, bothPositiveRight, movementHighRight,
                                 mengeAnVorzeichenwechselRight,
                                 avgAccX, avgAccY, avgAccZ, avgGyroX, avgGyroY, avgGyroZ,
                                 avgMagX, avgMagY, avgMagZ]
                            wr.writerow(values)
    print("done extracting features")


def buildPathsForPerson(person, requiredPath):
    paths = []
    #for i in range(len(activities)):
    for i in range(len(activities2)):
        #for n in range(1, 61):
        for n in range(1, 15):
            nr = str(n)
            if (n < 10):
                nr = "0" + str(n)
            #folderPath = requiredPath + "\\" + activities[i] + "\\" + "p" + str(person)
            folderPath = requiredPath + "\\" + activities2[i] + "\\" + "p" + str(person)
            #if requiredPath == target and not os.path.exists(folderPath):
            if requiredPath == target3 and not os.path.exists(folderPath):
                os.makedirs(folderPath)
            path = folderPath + "\\" + "s" + nr + "RL.csv"
            paths.append(path)

            path = folderPath + "\\" + "s" + nr + "LL.csv"
            paths.append(path)

    return paths


def scaleData(fromperson, personcount):
    #fV = pd.read_csv("fixedValuesToPerson.csv")
    fV = pd.read_csv("fixedValuesToPerson3.csv")
    for i in range(fromperson, personcount + 1):

        currentPersonFV = fV[fV.person == i]
        sourcePaths = buildPathsForPerson(i, initial)
        #targetPaths = buildPathsForPerson(i, target)
        targetPaths = buildPathsForPerson(i, target3)

        for sourcePath, targetPath in zip(sourcePaths, targetPaths):

            with open(targetPath, "w", newline='') as targetFile:
                wr = csv.writer(targetFile, quoting=csv.QUOTE_ALL)
                wr.writerow(categories)

                df = pd.read_csv(sourcePath)

                for index, row in df.iterrows():
                    rowToWrite = []
                    rowToWrite.append((row.AccX - currentPersonFV.AvgAccX.item()) / abs(
                        (currentPersonFV.MaxAccX.item() - currentPersonFV.AvgAccX.item())))

                    rowToWrite.append((row.AccY - currentPersonFV.AvgAccY.item()) / abs(
                        (currentPersonFV.MaxAccY.item() - currentPersonFV.AvgAccY.item())))

                    rowToWrite.append((row.AccZ - currentPersonFV.AvgAccZ.item()) / abs(
                        (currentPersonFV.MaxAccZ.item() - currentPersonFV.AvgAccZ.item())))

                    rowToWrite.append((row.GyroX - currentPersonFV.AvgGyroX.item()) / abs(
                        (currentPersonFV.MaxGyroX.item() - currentPersonFV.AvgGyroX.item())))

                    rowToWrite.append((row.GyroY - currentPersonFV.AvgGyroY.item()) / abs(
                        (currentPersonFV.MaxGyroY.item() - currentPersonFV.AvgGyroY.item())))

                    rowToWrite.append((row.GyroZ - currentPersonFV.AvgGyroZ.item()) / abs(
                        (currentPersonFV.MaxGyroZ.item() - currentPersonFV.AvgGyroZ.item())))

                    rowToWrite.append((row.MagX - currentPersonFV.AvgMagX.item()) / abs(
                        (currentPersonFV.MaxMagX.item() - currentPersonFV.AvgMagX.item())))

                    rowToWrite.append((row.MagY - currentPersonFV.AvgMagY.item()) / abs(
                        (currentPersonFV.MaxMagY.item() - currentPersonFV.AvgMagY.item())))

                    rowToWrite.append((row.MagZ - currentPersonFV.AvgMagZ.item()) / abs(
                        (currentPersonFV.MaxMagZ.item() - currentPersonFV.AvgMagZ.item())))

                    wr.writerow(rowToWrite)
    print("done scaling")

#scaleData(1, 10)
#generateFeatures(1, 10)
#scaleData(11, 11)
generateFeatures(11, 11)
