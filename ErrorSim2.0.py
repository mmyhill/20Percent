import random
import csv
# Purpose: The goal of ErrorSim2.0 is to simulate bit flips and explore methods for correcting them
#(and rewrite previous program with better technique/compiling more frequently)
# Author/s: Morgan Myhill
# 10/19/18
# On My Honor: MM
# Collaborators: Jude & Grant helped debugging

class errorSim:
    def __init__(self, toDo):
        #string of tasks in format:(2 digits!!!)numberOfRun)chanceOfErrorAsDecimal(<=1.00),copies*
        self.directions = open(toDo, "r").read()
        self.details = open("Details.txt","a")
        self.forExport = open("ForExport.csv","w")
        self.forExport.write("chanceErr" + ',' + "numCopies" + ',' + "numErrors" + ',' "uncaughtErrors" + '\n')
        self.calc()


    def calc(self):
        toDoNow = self.directions[0 : self.directions.find('\n')]

        runNum = toDoNow[0:toDoNow.find(')')]
        chanceErr = int(toDoNow[toDoNow.find(')') + 1 : toDoNow.find(',')])
        numCopies = int(toDoNow[toDoNow.find(',') + 1: len(toDoNow) - 1])

        randBin = self.genRand(runNum)

        arr = [["" for x in range(2)]for i in range(1000)]
        self.genError(numCopies, 1, runNum, randBin, arr, chanceErr)
        self.checkBasic(arr, randBin, numCopies, chanceErr)

        self.directions = self.directions[self.directions.find('\n') + 1 : len(self.directions)] #remove current line

        #recurse if needed:
        if(self.directions.count('*') > 0):
            self.calc()



    def genRand(self, numRun): #private
        randBin = ""
        for i in range(1000):
            randBin += "" + str(random.randint(0,1))
        self.details.write("Original Binary File for Run " + numRun + ":\n" + randBin + '\n')
        return randBin

    def genError(self, copsNeeded, thisCop, numRun, randBin, arr, chanceErr):
        thisErr = ''
        for i in range(1000):
            isOne = randBin[i] == '1'
            if(random.randint(1,100) <= chanceErr):
                isOne = not isOne
            if(isOne):
                thisErr += '1'
                arr[i][1] += str(thisCop) + " "
            else:
                thisErr += '0'
                arr[i][0] += str(thisCop) + " "
        self.details.write("Error File #" + str(thisCop) + " for Run " + str(numRun) + ":\n" + thisErr + '\n')
        if(thisCop < copsNeeded):
            self.genError(copsNeeded, thisCop + 1, numRun, randBin, arr, chanceErr)

    def checkBasic(self, arr, goldenCopy, numCopies, chanceErr):
        numErrors = 0
        uncaughtErrors = 0
        for x in range (len(arr)):
            correctAns = (goldenCopy[x] == '1')
            decidedAns = len(arr[x][1]) > len(arr[x][0])#should never be same length, requires odd # of requested copies
            if (correctAns): #if correct answer is 1
                numErrors += int(arr[x][0].count(' '))
                if(decidedAns != correctAns):
                    uncaughtErrors += int(arr[x][0].count(' '))
            else:#correct answer is 0
                numErrors += int(arr[x][1].count(' '))
                if(decidedAns != correctAns):
                    uncaughtErrors += int(arr[x][1].count(' '))
        self.forExport.write(str(chanceErr) + ',' + str(numCopies) + ',' + str(numErrors) + ','+ str(uncaughtErrors) + '\n')
            #numErrors should be very near chanceErr * 1000, still of relevance to see reliablity of random num generator

class CreateRandToDo:
    def __init__(self, length):
        self.length = length
        self.writeTo = open("toDo.txt", "w")
        self.gen()

    def gen(self):
        for x in range(self.length):
            self.writeTo.write(str(x) + ")" + str(random.randint(1, 50)) + "," + str(random.randint(1, 50)) + "*" + '\n')

def main():
    CreateRandToDo(1000)
    errorSim("toDo.txt")

if __name__ == "__main__":
        main()


#add method to determine actual probablity of error based on altitude, etc.
