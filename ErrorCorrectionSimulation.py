# Purpose: The goal of ErrorSim2.0 is to simulate bit flips and explore methods for correcting them
# while also learning Python
# Author/s: Morgan Myhill
# 10/10/18
# On My Honor: MM
# Collaborators: none
class sim:

    def __init__(self, toDo):
        #toDo will be file read in containing simulation conditions
        #string of tasks in format:numberOfRun)chanceOfErrorAsDecimal(<=1.00) copies
        self.directions = open(toDo, "r").read()
        self.details = open("Details.txt","w")
        self.forExport = open("ForExport.txt","w")

    def calc(self):
        #recursive
        toDoNow = directions[directions.find(')'): directions.find('/n')]#will be next line of file
        print(toDoNow)
        #write vertical column to file for easy paste into google sheets to create graphs

        #CREATE BINARY FILE
        randBin = ""
        for i in range(1000):
            randBin += "" + str(random.randint(0,2))

        self.details.append("Original Binary File for Run" + toDoNow[toDoNow[0]:toDoNow.find(")")] + ":\n" + randBin)

        #CHECK CONDITIONS
        chanceFlip = int(toDoNow[toDoNow.find('.')]:toDoNow.find(' ')])
        numCops = int(toDoNow[toDoNow.find(' ') + 1:toDoNow.find('\n')])
        runNum = self.directions[0:self.directions.find(')')]

        #INDUCE ERRORS INTO ALL FILES
        self.generateFlip(randBin, numCops, chance, runNum)

        if(self.directions.find('\n') > -1):
            self.directions = self.directions[string.find("\n"):len(self.directions)]
            self.calc()

    def generateFlip(self, randBin, numCopies, chance, runNum):
        if(numCopies <= 0):
            self.compFilesSIMPLEST("Run # " + runNum + " Error Binary File copy # " + 1 + ":/n" + err + "end")
            break
        err = ""
            for i in range(len(randBin)):
                useNow = if(randBin[i] == '1')
                if(random.randint(1,101) < 100 * chance):
                    useNow = !useNow
                if(useNow):
                    err += "1"
                else:
                    err += "0"

        self.details.append("Run # " + runNum + " Error Binary File copy # " + numCopies + ":/n" + err + "end")

        self.generateFlip(randBin, numCopies - 1, chance)

    def compFilesSIMPLEST(self, randBinToFind): # Distance[i][j][k] == distance = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
        ans = [["" for i in range(2)]for j in range(len(randBinToFind))] # 3D array of strings ???

        self.compFilesRecurs(ans, randBinToFind)

        predictedFinal = ""
        numBitsPredictedIncorrect = 0
        numBitsCorrectedIncorrectly = 0
        totalBitsChecked = 0

        for(i in range(len(randBinToFind))):#tries to correct in addition to comparing correction to actual
            if(len(ans[i][0]) > len(ans[i][1]):
                predictedFinal += "0"
                numBitsPredictedIncorrect += len(ans[i][1])/2
            else:
                predictedFinal += "1"
                numBitsPredictedIncorrect += len(ans[i][0])/2
            if(predictedFinal[i] != randBinToFind[i]):
                numBitsCorrectedIncorrectly += len(ans[i][0]) + len(ans[i][1])
            totalBitsChecked += len(ans[i][0]) + len(ans[i][1])

        self.forSheets.write()

    def compFilesRecurs(self, ans, lookFor): #will find give starting or ending index? *Written as if starting*
        use = self.details[self.details.find(lookFor) + len(lookFor):self.details.find("end")]
        copyNum = lookFor[lookFor.find("Error Binary File copy # ") + 1:lookFor.find(":")]
        for(i in range(len(use))):
            charCheck = use[i]
            if(charCheck == '0'):
                ans[i][0] += copyNum + ","#number of matching files will be string length/2
            elif(charCheck == '1'):
                ans[i][1] += copyNum + ","
            else:
                print "something wrong, correct error"

        lookFor = lookFor[lookFor.find("end") + 3:len(lookFor)]

        if(lookFor.find("Run # ") >= 0):
            self.compFilesRecurs(ans, lookFor)

        #*can you change data outside the scope of method? (in Java, you can't modify inputs???)

def main():
    simClass = sim(ToDo.txt)
if __name__ == "__main__":
        main()
