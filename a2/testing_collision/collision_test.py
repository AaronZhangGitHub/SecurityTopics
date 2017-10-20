import json
import os
import hashlib

STUDENT_FILES = "./StudentFiles_collision"
def main():
    filesToTest = runOverFilesInLocalDirectory(STUDENT_FILES)
    testFilesCollision(filesToTest)

def testFilesCollision(filesToRun):
    for fileName in filesToRun:
        timeout = time.time() + 20
        studentOnyen = fileName.split('_')
        hashVals = getHashValues(fileName)
        hashToSameValue_first24Bits = collisionTest(hashVals[0],hashVals[1])
        print("%s %s"%(studentOnyen[1],hashToSameValue_first24Bits))

def getHashValues(fileName):
    hashVal = hashlib.sha256()
    hashVal2 = hashlib.sha256()
    outputVal = os.popen("python3 %s/%s"%(STUDENT_FILES,fileName)).read().rstrip()
    outputSplit = outputVal.split(' ')
    return outputSplit

def collisionTest(hash1, hash2):
    t1 = hashlib.sha256(hash1.encode('utf-8')).hexdigest()
    t2 = hashlib.sha256(hash2.encode('utf-8')).hexdigest()
    return (t1[:6]==t2[:6])

def runOverFilesInLocalDirectory(directory):
    tempList = [];
    for fileName in os.listdir(directory):
        tempList.append(fileName)
    return tempList

main()
