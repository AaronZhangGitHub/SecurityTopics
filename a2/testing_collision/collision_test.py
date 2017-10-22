import json
import os
import hashlib
import subprocess

STUDENT_FILES = "./student_submissions"
grades = {}
def main():
    studentDirectoryList = getStudentDirectoryList()
    runTest(studentDirectoryList)
    with open("collision_grades.json",'w') as fileToWrite:
        json.dump(grades,fileToWrite)

def getStudentDirectoryList():
    studentDirectories = []
    for root, dirs, files in os.walk(STUDENT_FILES):
        studentDirectories = dirs
        break
    return studentDirectories

def runTest(studentDirectories):
    for studentDir in studentDirectories:
        submissionFolder = "%s/%s/Submission attachment(s)"%(STUDENT_FILES,studentDir)
        temp = os.listdir(submissionFolder)
        studentOnyen = studentDir[studentDir.find('(')+1:studentDir.find(')')]
        print(studentOnyen)
        if(len(temp)==0):
            #students get 0
            grades[studentOnyen] = 0
        else:
            preImageTest(submissionFolder,studentOnyen)

def preImageTest(submissionFolder,onyen):
    proc = subprocess.Popen(["python3","%s/a2_%s_collision.py"%(submissionFolder,onyen)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        output, errs = proc.communicate()
        grades[onyen] = 0
        return
    except Exception as e:
        proc.kill()
        output, errs = proc.communicate()
        grades[onyen] = 0
        return
    output = output.decode('UTF-8').rstrip()
    hashVals = output.split(' ') #delim on space
    if len(hashVals)<2:
        grades[onyen] = 0
        return
    hashToSameValue_first24Bits = collisionTest(hashVals[0],hashVals[1])
    if hashToSameValue_first24Bits:
        grades[onyen] = 1
    else:
        grades[onyen] = 0

def collisionTest(hash1, hash2):
    t1 = hashlib.sha256(hash1.encode('utf-8')).hexdigest()
    t2 = hashlib.sha256(hash2.encode('utf-8')).hexdigest()
    return (t1[:6]==t2[:6])

def toSixChar(inputStr):
    return inputStr[:6]
main()
#####################
