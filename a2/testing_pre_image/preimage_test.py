import subprocess
import json
import os
import hashlib

TEST_STR = "Aaron"
STUDENT_FILES = "./student_submissions"
grades = {}
def main():
    hashVal = toSixChar(hashlib.sha256(TEST_STR.encode('utf-8')).hexdigest())
    studentDirectoryList = getStudentDirectoryList()
    runTest(studentDirectoryList, hashVal)
    with open("preimage_grades.json",'w') as fileToWrite:
        json.dump(grades,fileToWrite)

def getStudentDirectoryList():
    studentDirectories = []
    for root, dirs, files in os.walk(STUDENT_FILES):
        studentDirectories = dirs
        break
    return studentDirectories

def runTest(studentDirectories,hashVal):
    for studentDir in studentDirectories:
        submissionFolder = "%s/%s/Submission attachment(s)"%(STUDENT_FILES,studentDir)
        temp = os.listdir(submissionFolder)
        studentOnyen = studentDir[studentDir.find('(')+1:studentDir.find(')')]
        print(studentOnyen)
        if(len(temp)==0):
            #students get 0
            grades[studentOnyen] = 0
        else:
            preImageTest(submissionFolder,studentOnyen,hashVal)

def preImageTest(submissionFolder,onyen,hashVal):
    fileToRun = "%s/a2_%s_preimage.py"%(submissionFolder,onyen)
    proc = subprocess.Popen(["python3",fileToRun,hashVal], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errs = proc.communicate(timeout=300)
    except subprocess.TimeoutExpired:
        proc.kill()
        output, errs = proc.communicate()
        grades[onyen] = 0
        return
    output = output.decode('UTF-8').rstrip()
    studentHashVal = hashlib.sha256(output.encode('utf-8')).hexdigest()
    studentHashVal = toSixChar(studentHashVal)
    if studentHashVal==hashVal:
        grades[onyen] = 1
    else:
        grades[onyen] = 0

def readJsonFile(fileName):
    with open(fileName) as json_data:
        jsonFile = json.load(json_data)
        return jsonFile

def toSixChar(inputStr):
    return inputStr[:6]

main()
#####################
