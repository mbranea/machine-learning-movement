import numpy as np
import pandas as pd
import csv


initial = "isolatedData"
#activities =["jumping","walking","standing"]
activities =["unbekannt",]
testPersons = ["p11"]
categories = ["AccX","AccY","AccZ","GyroX","GyroY","GyroZ","MagX","MagY","MagZ"]

#inputacti =["j"]
#inputpersons = ["1"]

inputacti =["j","l","s"]
#inputpersons = ["1","2"]
inputpersons = ["3"]

def buildPaths():
    paths = []
    for i in range(len(inputacti)):
        for p in range(len(inputpersons)):
                path = "beltdata" + "\\" +inputpersons[p]+ inputacti[i]+  "l" + ".txt"
                paths.append(path)
                path = "beltdata" + "\\" +inputpersons[p]+ inputacti[i] + "r" +  ".txt"
                paths.append(path)
    return paths


def buildPathsnoAcc():
    paths = []
    for p in range(len(inputpersons)):
                path = "beltdata" + "\\" +inputpersons[p]+ "l" + ".txt"
                paths.append(path)
                path = "beltdata" + "\\" +inputpersons[p] + "r" +  ".txt"
                paths.append(path)
    return paths

def buildPathsout():
    paths = []
    for i in range(len(activities)):
        for p in range(len(testPersons)):
            for n in range(1,15):
                nr=str(n)
                if(n<10):
                    nr="0"+str(n)
                path = initial + "\\" + activities[i] + "\\" + testPersons[p] + "\\" + "s" + nr + "LL.csv"
                paths.append(path)
            for n in range(1,15):
                nr=str(n)
                if(n<10):
                    nr="0"+str(n)
                path = initial + "\\" +activities[i]+ "\\" +testPersons[p] + "\\" + "s" + nr + "RL.csv"
                paths.append(path)
    return paths


def beltTo25Hz():
    hz25row = []
    inpath = buildPathsnoAcc()
    outpath = buildPathsout()
    startrow = " "
    for k in range(len(inpath)):
        with open(inpath[k]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            startflag = 1
            for d in range(1,15):
                filestring = outpath[d-1 + (14 * k)]
                print(filestring)
                #print("\n" , d-1 + (60 * k) )
                #continue
                #filestring = "Test\\Test"+str(d)+".csv"
                with open(filestring, "w", newline='') as myfile:
                    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                    line_count = 1
                    temp_rows = []
                    for row in csv_reader:
                        if startflag == 1:
                            print(f'Column names are {" <".join(row)}')
                            startflag = 0
                            del row[0]
                            del row[3]
                            del row[-3:-1]
                            del row[-1]
                            startrow = categories
                        else:
                            if  line_count == 1:
                                wr.writerow(startrow)

                            if (line_count)%4 != 0:
                                temp_rows.append(row)
                            else:
                                #print("linecount ",line_count)
                                temp_rows.append(row)
                                #print(temp_rows)
                                for i in range(1,11):
                                    if i ==4:
                                        continue
                                    array = []
                                    for j in range (0,4):
                                        array.append(float(temp_rows[j][i].replace(',', '.')))
                                    #array.append(float(temp_rows[1][i].replace(',', '.')))
                                    #array.append(float(temp_rows[2][i].replace(',', '.')))
                                    #array.append(float(temp_rows[3][i].replace(',', '.')))

                                    #print("array  ", array)
                                    #print("MEAN  ", np.median(array))
                                    hz25row.append(np.median(array))

                                temp_rows = []
                                temp_x = hz25row[0]
                                hz25row[0] = hz25row[1]
                                hz25row[1] = temp_x

                                temp_x = hz25row[3]
                                hz25row[3] = hz25row[4]
                                hz25row[4] = temp_x

                                temp_x = hz25row[6]
                                hz25row[6] = hz25row[7]
                                hz25row[7] = temp_x
                                wr.writerow(hz25row)
                                hz25row = []
                            #print(f'\t{row[0]}| {row[1]}| {row[2]}')
                            line_count += 1
                            if line_count == 501:
                                break

                print(f'Processed {line_count} lines.')
            #dataFile = pd.read_csv(path)
            #print(dataFile)




print("TEST")
buildP = buildPathsnoAcc()
print(buildP , " " , len(buildP))
print(buildPathsout() , " " , len(buildPathsout()))
beltTo25Hz()