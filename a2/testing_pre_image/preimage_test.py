import json
import os
import hashlib
import subprocess

STUDENT_FILES = "./StudentFiles"
TEST_STR = "Aaron"

def main():
    filesToTest = runOverFilesInLocalDirectory(STUDENT_FILES)
    hashVal = toSixChar(hashlib.sha256(TEST_STR.encode('utf-8')).hexdigest())
    preImageTest(hashVal,filesToTest)

def preImageTest(hashVal, filesToTest):
    for studentFile in filesToTest:
        proc = subprocess.Popen(["python3","%s/%s"%(STUDENT_FILES,studentFile),hashVal], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, errs = proc.communicate(timeout=300)
        except subprocess.TimeoutExpired:
            proc.kill()
            output, errs = proc.communicate()
            #student failed
            continue
        output = output.decode('UTF-8').rstrip()
        studentHashVal = hashlib.sha256(output.encode('utf-8')).hexdigest()
        studentHashVal = toSixChar(studentHashVal)
        if studentHashVal==hashVal:
            #students solution is correct
        else:
            #student failed

def toSixChar(inputStr):
    return inputStr[:6]
def runOverFilesInLocalDirectory(directory):
    tempList = [];
    for fileName in os.listdir(directory):
        tempList.append(fileName)
    return tempList

main()
