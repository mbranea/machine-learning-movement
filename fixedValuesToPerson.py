import pandas as pd
import csv
initial = "isolatedData"
activities =["jumping","standing","walking"]
activities2 = ["unbekannt"]
#testPersons = ["p1","p2","p3","p4","p5","p6","p7","p8","p9","p10"]
testPersons2 = ["p1","p2","p3","p4","p5","p6","p7","p8"]
testPersons3 = ["p11"]
categories = ["AccX","AccY","AccZ","GyroX","GyroY","GyroZ","MagX","MagY","MagZ"]
averageCategories = ["AvgAccX","AvgAccY","AvgAccZ","AvgGyroX","AvgGyroY","AvgGyroZ","AvgMagX","AvgMagY","AvgMagZ"]
maxCategories = ["MaxAccX","MaxAccY","MaxAccZ","MaxGyroX","MaxGyroY","MaxGyroZ","MaxMagX","MaxMagY","MaxMagZ"]

def buildPathsForPerson(person):
    paths = []
    for i in range(len(activities2)):
        for n in range(1,15):
            nr=str(n)
            if(n<10):
                nr="0"+str(n)
            #path = initial + "\\" +activities[i]+ "\\" +testPersons[person] + "\\" + "s" + nr + "RL.csv"
            path = initial + "\\" + activities2[i] + "\\" + testPersons3[person] + "\\" + "s" + nr + "RL.csv"
            paths.append(path)
            #path = initial + "\\" + activities[i] + "\\" + testPersons[person] + "\\" + "s" + nr + "LL.csv"
            path = initial + "\\" + activities2[i] + "\\" + testPersons3[person] + "\\" + "s" + nr + "LL.csv"
            paths.append(path)

    return paths


#with open("FixedValuesToPerson.csv", "w", newline='') as myfile:
with open("FixedValuesToPerson3.csv", "w", newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["person"]+maxCategories+averageCategories)
    #for i in range(0,10):
    for i in range(0, 1):
        maxArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        averageArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        count=0
        for path in buildPathsForPerson(i):
            dataFile = pd.read_csv(path)
            count+=125

            maxArray[0]=  max(maxArray[0], max(abs(dataFile.AccX)))
            maxArray[1] = max(maxArray[1], max(abs(dataFile.AccY)))
            maxArray[2] = max(maxArray[2], max(abs(dataFile.AccZ)))
            maxArray[3] = max(maxArray[3], max(abs(dataFile.GyroX)))
            maxArray[4] = max(maxArray[4], max(abs(dataFile.GyroY)))
            maxArray[5] = max(maxArray[5], max(abs(dataFile.GyroZ)))
            maxArray[6] = max(maxArray[6], max(abs(dataFile.MagX)))
            maxArray[7] = max(maxArray[7], max(abs(dataFile.MagY)))
            maxArray[8] = max(maxArray[8], max(abs(dataFile.MagZ)))

            averageArray[0] = sum([averageArray[0], sum(dataFile.AccX)])
            averageArray[1] = sum([averageArray[1], sum(dataFile.AccY)])
            averageArray[2] = sum([averageArray[2], sum(dataFile.AccZ)])
            averageArray[3] = sum([averageArray[3], sum(dataFile.GyroX)])
            averageArray[4] = sum([averageArray[4], sum(dataFile.GyroY)])
            averageArray[5] = sum([averageArray[5], sum(dataFile.GyroZ)])
            averageArray[6] = sum([averageArray[6], sum(dataFile.MagX)])
            averageArray[7] = sum([averageArray[7], sum(dataFile.MagY)])
            averageArray[8] = sum([averageArray[8], sum(dataFile.MagZ)])


        averageArray = [x / count for x in averageArray]
        maxArray = [i+1]+ maxArray
        wr.writerow(maxArray+averageArray)
    print("done")
