import math
import random
import string

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Push(self,item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items[len(self.items) - 1]

    def Size(self):
        return len(self.items)
    
def matches(open,close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)

def parChecker(symbolString):

    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.Push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.Pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def baseConverter(decNumber,base):

    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.Push(int(rem))
        decNumber = math.floor(decNumber / base)

    newString = ""
    while not remstack.isEmpty():
        newString = newString + str(digits[remstack.Pop()])
    return newString

def infixToPostfix(infixexpr):

    if type(infixexpr) != str:
        return "this is not a string!"

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    print(opStack.isEmpty())
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token.isalnum():
            postfixList.append(token)
        elif token == "(":
            opStack.Push(token)
        elif token == ")":
            topToken = opStack.Pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.Pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.Peek()] >= prec[token]):
                postfixList.append(opStack.Pop())

            opStack.Push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.Pop())

    return " ".join(postfixList)

def postfixEval(postfixExpr):

    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.Push(token)
        else:
            operator2 = operandStack.Pop()
            operator1 = operandStack.Pop()
            result = doMath(token,operator1,operator2)
            operandStack.Push(result)
    return operandStack.Pop()

def doMath(op,op1,op2):

    PrecList = ["*","/","+","-"]
    if op in PrecList:
        return eval("".join([op1,op,op2]))

def infixEval(infixStr):
    
    infixStr = infixToPostfix(infixStr)
    result = postfixEval(infixStr)
    return result

postFixstr = infixEval("5 + 9")
print(postFixstr)

##Exec: python C:\Users\Mbwenga\Documents\ML\Python\Stack.py

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)  

def hotPotato(namelist, N):

    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(N):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

class flippedQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(len(self.items) - 1,item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)  

base = 16
hexa = baseConverter(233,base)
print(hexa)

names = ['Pascal','Tesla','Newton','Tao','Neumann']
print(hotPotato(names,12))


chkstr = "(()())"

print(parChecker(chkstr))


#exec: python C:\\Users\\Mbwenga\\Documents\\ML\\Python\\Stack.py


class Printer:
    def __init__(self,pages):
        self.pagerate = pages
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining == 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * (60 / self.pagerate)

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingTimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averegeWait = sum(waitingTimes)/float(len(waitingTimes))
    print("Average Wait Time: {} seconds".format(averegeWait) + " Tasks Remaining {}".format(printQueue.size()))

#volume limit = amount of cars per second that can be processed through road
class Road:
    def __init__(self,VolumeLimit):
        self.VolumeLimit = VolumeLimit
        self.currentVolume = None
        self.timeRemaining = 0

    def Tick(self):
        if self.currentVolume != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining == 0:
                self.currentVolume == None

    def Busy(self):

        if self.currentVolume == None:
            return True
        else:
            return False

    def startNext(self,newLoad):
        self.currentVolume == newLoad
        self.timeRemaining = int(newLoad.getVolume() / VolumeLimit)

#Distance = distance of road segment to traverse
class Load:
    def __init__(self,time):
        self.timestamp = time
        self.Volume = random.randrange(1000,3300)

    def getStamp(self):
        return self.timestamp

    def getVolume(self):
        return self.Volume

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

#numSeconds = number of seconds to simulate
def TrafficSimulation(numSeconds, CarsPerSecond):
    road = Road(CarsPerSecond)
    TrafficQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newLoad():
            load = Load(currentSecond)
            TrafficQueue.enqueue(load)

        if (not road.Busy()) and (not TrafficQueue.isEmpty()):
            nextLoad = TrafficQueue.dequeue()
            waitingTimes.append(nextLoad.waitTime(currentSecond))
            road.startNext(nextLoad)

        road.Tick()
    if len(waitingTimes) != 0:
        averegeWait = sum(waitingTimes)/float(len(waitingTimes))
        print("Average Wait Time: {} seconds".format(averegeWait) + " Tasks Remaining {}".format(TrafficQueue.size()))

def newLoad():
    num = random.randrange(1,171)
    if num == 170:
        return True
    else:
        return False 

for i in range(10):
    TrafficSimulation(3600,5)

##Exec: python C:\Users\Mbwenga\Documents\ML\Python\Stack.py 
[]
#Reasoning behind traffic simulator(assumptions):
#Number of roads in stockholm: 170
#https://spa.merinfo.se/question/hur-manga-gator-och-vagar-finns-det-i-stockholms-lan-erik-lindeberg
#Average road length = average length driven/day: https://www.trafa.se/vagtrafik/
#I.e, if drivers were to choose their paths arbitrarly and this road being simulated happened to be one of them.
#random amount of drivers will also be entering.
#Traffic load calculated assuming average distance between cars = 10m.

#Conclusions:
#This is for obvious reasons not accurate(random driving patterns, road lenghts, ignoring splits/mergins of roads etc)
#It was mainly constructed for improving my understanding of queues, stacks etc