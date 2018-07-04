import math
import time
import random

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentValue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentValue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentValue

#Gottim = [1,2,3,4,5]

#insertionSort(Gottim)

#print(Gottim)

unpure_list = [1,5,6,4,3,2]

#insertionSort(unpure_list)

# c print(unpure_list)

def mergeSort(alist):
    print("Splitting {}".format(alist))
    if len(alist)>1:
        mid = math.floor(len(alist)/2)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("merging",alist)

#mergeSort(unpure_list)

def SeqSearch(alist,item):

    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if item == alist[pos]:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = math.floor(len(alist)/2)
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

def iterBinarySearch(alist,item):

    First = 0
    Last = len(alist) - 1
    Found = False

    while First<=Last and not Found:
        midpoint = math.floor((First+Last)/2)

        if alist[midpoint] == item:
            Found = True
        else:
            if item<alist[midpoint]:
                Last = midpoint - 1
            else:
                First = midpoint+1

    return Found

def binVseq(alist,acake):
    print("Running the simulation...")
    orgTime = time.clock()
    
    binTruth = binarySearch(alist,acake)
    binTime = time.clock() - orgTime

    seqTruth = SeqSearch(alist,acake)
    seqTime = time.clock() - (orgTime + binTime)
    
    print("Binary Search took {}, and Sequential Search took {} for length {} list".format(binTime,seqTime,len(alist)))

    if not (binTruth and seqTruth):
        print("And also, the cake was a lie.")

#python C:\Users\Mbwenga\Documents\ML\Python\BigO.py
#Exec: C:\\Users\\Mbwenga\\Documents\\ML\\Python\\BigO.py

def iterVrec(alist,item):

    print("Running iterative vs recursive binary search...")
    orgTime = time.clock()

    iterTruth = iterBinarySearch(alist,item)
    iterTime = orgTime - time.clock()

    recTruth = binarySearch(alist,item)
    recTime = orgTime -(iterTime + time.clock())

    print("Iterative search took {}, and recursive search {}".format(iterTime,recTime))

therange = 50000
thecake = random.randrange(therange)
massiveList = [an_i for an_i in range(therange)]

#binVseq(massiveList,thecake)

#print(iterVrec(massiveList,thecake))

class HashTable:
    def __init__(self,size):
        self.slots = [None]*size
        self.data = [None]*size

    def __getitem__(self,item):
        return self.Search(item)

    def __setitem__(self,item,data):
        self.Store(item,data)

    def Store(self,item,data):
        hashvalue = self.hashfunction(item,len(self.slots))

        if self.slots[hashvalue]==None:
            self.slots[hashvalue] = item
            self.data[hashvalue] = data
        else:
            #externally implemented quadratic probing
            quadenum = 1
            nextslot = self.rehash(hashvalue,len(self.slots))

            while self.slots[nextslot]!=None:
                quadenum = (quadenum + 1)**2 - 1
                nextslot = self.rehash(nextslot + quadenum,len(self.slots))

            self.slots[nextslot]=item
            self.data[nextslot]=data

    def hashfunction(self,item,size):
        return item%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def Search(self,item):
        try:
            Delbool=item[1]
            item=item[0]
        except TypeError:
            Delbool=False

        startslot = self.hashfunction(item,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position]!=None and not found and not stop:
            if self.slots[position]==item:
                found=True
                data=self.data[position]
                if Delbool:
                    self.data[position]=None
                    self.slots[position]=None
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def Delete(self,item):
        self.Search([item,True])

H1 = HashTable(12)

H1[21] = "Table"

print(H1[21])
print(H1.slots,H1.data)


def HashTrial(Htable,InptDta):
    for element in range(InptDta[0]):
        SplitVal = list(InptDta[1])
        Htable[element] = "".join(random.sample(SplitVal,len(SplitVal)))

    print("HashTable has been filled with {} values!".format(InptDta[0]))
    print(Htable.slots,Htable.data)

sizeOfTabel = 19
WordtoObfuscate = "DoYouKnowThePythonicWay?"
HashTrial(HashTable(sizeOfTabel),[sizeOfTabel,WordtoObfuscate])
     

