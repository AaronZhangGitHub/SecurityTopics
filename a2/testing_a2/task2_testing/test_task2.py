import subprocess
import json
import os

TEST_FILE = "./test_task2_cases.json"
STUDENT_FILES = "./student_submissions"
grades = {}
def main():
    jsonRepresentation = readJsonFile(TEST_FILE)
    studentDirectoryList = getStudentDirectoryList()
    runTest(studentDirectoryList,jsonRepresentation)
    with open("hamming_grades.json",'w') as fileToWrite:
        json.dump(grades,fileToWrite)


def getStudentDirectoryList():
    studentDirectories = []
    for root, dirs, files in os.walk(STUDENT_FILES):
        studentDirectories = dirs
        break
    return studentDirectories

def runTest(studentDirectories,jsonRepresentation):
    for studentDir in studentDirectories:
        submissionFolder = "%s/%s/Submission attachment(s)"%(STUDENT_FILES,studentDir)
        temp = os.listdir(submissionFolder)
        studentOnyen = studentDir[studentDir.find('(')+1:studentDir.find(')')]
        print(studentOnyen)
        if(len(temp)==0):
            #students get 0
            grades[studentOnyen] = 0
        else:
            hammingTest(jsonRepresentation,submissionFolder,studentOnyen)

def hammingTest(jsonTestCaseRep,submissionFolder,onyen):
    tests = jsonTestCaseRep['tests']
    totalTestNumber = len(tests)
    totalIncorrect = 0
    fileToRun = "%s/a2_%s_hamming.py"%(submissionFolder,onyen)
    for test in tests:
        arg1 = test['inputArg1']
        arg2 = test['inputArg2']
        trustTheProcess = subprocess.Popen(["python3",fileToRun,arg1,arg2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output,errs = trustTheProcess.communicate(timeout=5)
        except:
            print("Error",onyen)
            totalIncorrect+=1
            grades[onyen] = "Error"
            trustTheProcess.kill()
            output,errs = trustTheProcess.communicate(timeout=5)
            continue
        output = output.decode('UTF-8').rstrip()
        errs = errs.decode('UTF-8').rstrip()
        expectedOutput = test['output']
        if(errs!=""):
            totalIncorrect+=1
        trustTheProcess.kill()
    grade = (totalTestNumber - totalIncorrect)/totalTestNumber
    grades[onyen] = grade

def readJsonFile(fileName):
    with open(fileName) as json_data:
        jsonFile = json.load(json_data)
        return jsonFile
main()
