class BingoSheet:
    def __init__(self, sheet: list):
        self.sheet = sheet
        self.indices = []
        self.done = False

    def setTrue(self, num):
        for x in range(0, 5):
            for y in range(0, 5):
                if self.sheet[x][y] == num:
                    self.indices.append(x*5+y)

    def checkForWin(self):
        for x in range(0, 5):
            if all(y in self.indices for y in [x, 5+x, 10+x, 15+x, 20+x]):
                return True
            if all(y in self.indices for y in [5*x, 5*x+1, 5*x+2, 5*x+3, 5*x+4]):
                return True

    def unmarkedSum(self):
        runningSum = 0
        for x in range(0, 25):
            if x not in self.indices:
                runningSum += int(self.sheet[x // 5][x % 5])
        return runningSum
        
inputter = open("Gogogadget/AdventOfCode/day4/input.txt")
listacle = inputter.readline().split(",")
arrayList = []
numbersSoFar = []

while True:
    checkLine = inputter.readline()

    if not checkLine:
        break

    bingoSheet = []

    for x in range(0, 5):
        bingoSheet.append(inputter.readline().removesuffix("\n").split(" "))
        
        while bingoSheet[-1].count("") != 0:
            bingoSheet[-1].remove("")

    arrayList.append(BingoSheet(bingoSheet))

def part1(listacle: list, arrayList: list):
    for z in listacle:
        for g in arrayList:
            g.setTrue(z)
            if g.checkForWin():
                return g.unmarkedSum() * int(z)


def part2(listacle: list, arrayList: list):
    finalVal = 0
    for z in listacle:
        for g in arrayList:
            g.setTrue(z)
            if g.checkForWin() and not g.done:
                finalVal = g.unmarkedSum() * int(z)
                g.done = True
    return finalVal


print(str(part1(listacle, arrayList) ) + " is the first bingo!")
print(str(part2(listacle, arrayList) ) + " is the second bingo!")
