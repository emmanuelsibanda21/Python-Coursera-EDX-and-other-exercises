numBuckets = 47
def create():
    global numBuckets
    hSet= []
    for i in range(numBuckets):
        hSet.append([])
        return hSet
def hasElem(e):
    global numBuckets
    return e%numBuckets
def insert(hSet, i):
    global numBuckets
    hSet[hashElem(i)].append(i)
def remove(hSet, i):
    newBucket=[]
    for j in hSet[hashElem(i)]:
        if j !=i:
            newBucket.append(j)
            hSet[hashElem(i)] = newNucket
def member(hSet, i):
    return i in hSet[hashElem(i)]
nuBuckets = 47
def test1():
    s = create()
