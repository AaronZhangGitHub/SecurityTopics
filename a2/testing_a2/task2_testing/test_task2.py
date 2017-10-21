import subprocess
import json
import os

TEST_FILE = "./test_task2_cases.json"
STUDENT_FILES = "./StudentFiles_task2"

def main():
    jsonRepresentation = readJsonFile(TEST_FILE)
    studentFilesToRun = runOverFilesInLocalDirectory(STUDENT_FILES)
    testFiles(jsonRepresentation,studentFilesToRun)

def testFiles(jsonTestCaseRep, filesToTest):
    tests = jsonTestCaseRep['tests']
    totalTestNumber = len(tests)
    for file in filesToTest:
        studentOnyen = file.split('_')
        totalIncorrect = 0
        for test in tests:
            arg1 = test['inputArg1']
            arg2 = test['inputArg2']
            #outputVal = os.popen('python3 ./StudentFiles_task2/%s %s %s' % (file,arg1,arg2)).read().rstrip()
            proc = subprocess.Popen(["python3","%s/%s"%(STUDENT_FILES,file),arg1,arg2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                output, errs = proc.communicate(timeout=5)
            except:
                proc.kill()
                output, errs = proc.communicate()
            output = output.decode('UTF-8').rstrip()
            errs = errs.decode('UTF-8').rstrip()
            expectedOutput = test['output']
            if(errs!=""):
                totalIncorrect+=1
            proc.kill()
        print("%s Incorrect: %i out of %i total, score of " % (studentOnyen[1],totalIncorrect,totalTestNumber)) #this will late output information to a file

def readJsonFile(fileName):
    with open(fileName) as json_data:
        jsonFile = json.load(json_data)
        return jsonFile

def runOverFilesInLocalDirectory(directory):
    tempList = [];
    for fileName in os.listdir(directory):
        tempList.append(fileName)
    return tempList

main()
