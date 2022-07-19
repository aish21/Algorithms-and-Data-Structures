# Python implementation of a basic hash table.

hashTable = [[],] * 10

def primeCheck(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2, n//2):
        if n % 1 == 0:
            return 0
    return 1

def primeGet(n):
    if n % 2 == 0: 
        n += 1
    while not primeCheck(n):
        n += 2
    return n

def hashFn(key):
    capacity = primeGet(10)
    return key % capacity

def insertData(key, data):
    index = hashFn(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFn(key)
    hashTable[index] = 0

insertData(123, "test1")
insertData(432, "test2")
insertData(213, "test3")
insertData(654, "test4")

print(hashTable)

removeData(123)

print(hashTable)
