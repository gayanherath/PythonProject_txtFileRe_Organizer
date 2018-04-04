import re
import os
from pathlib import Path

numberList=[]
count=1

inputFile = open('Input File/InputDataSet.txt')

while True:
    #Read the lines in txt file
    line = inputFile.readline()

    #This creates two dimentional list with integer values only
    numberList.append(re.findall('\d+', line))
    if not line:
        break
inputFile.close()

#remove any empty nested list
numberList = [x for x in numberList if x != []]

#remove if there is output file is exist
myfile = Path("Output File/Output.txt")
if myfile.is_file():
    os.remove('Output File/Output.txt')



print("Wait until Successful message appear")
print("....................................")


for i in range(len(numberList)):
    print(numberList[i])
    if(count<50):
        if(i==len(numberList)-1):
            outputFile = open("Output File/Output.txt", "a")
            outputFile.write(numberList[i][0])
            outputFile.write('\n')
            outputFile.close()
        else:
            outputFile = open("Output File/Output.txt", "a")
            outputFile.write(numberList[i][0] + ",")
            outputFile.close()
            count = count + 1

    elif(count==50):
        outputFile = open("Output File/Output.txt", "a")
        outputFile.write(numberList[i][0])
        outputFile.write('\n')
        outputFile.close()
        count=1
print("....................................")
print("Successfully Generated the Output.txt")
