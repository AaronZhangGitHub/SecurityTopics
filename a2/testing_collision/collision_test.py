import json
import os
import hashlib
import subprocess

STUDENT_FILES = "./StudentFiles_collision"
def main():
    filesToTest = runOverFilesInLocalDirectory(STUDENT_FILES)
    testFilesCollision(filesToTest)


def testFilesCollision(filesToRun):
    for fileName in filesToRun:
        print(fileName)
        studentOnyen = fileName.split('_')
        hashVals = getHashValues(fileName)
        if (hashVals[0]=="Timeout") or (hashVals[1]=="Error"):
            print("%s program had an error running their program."%studentOnyen[1])
        else:
            hashVals = hashVals[0].split(' ') #delim on space
            print(hashVals)
            hashToSameValue_first24Bits = collisionTest(hashVals[0],hashVals[1])
            print("%s %s"%(studentOnyen[1],hashToSameValue_first24Bits))

def getHashValues(fileName):
    proc = subprocess.Popen(["python3","%s/%s"%(STUDENT_FILES,fileName)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        output, errs = proc.communicate()
        return ["Timeout","Timeout"]
    except Exception as e:
        proc.kill()
        output, errs = proc.communicate()
        return ["Error",e]
    #If output is valid, decode and strip newline
    output = output.decode('UTF-8').rstrip()
    errs = errs.decode('UTF-8').rstrip()
    returnTupule = [output,errs]
    return returnTupule

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
