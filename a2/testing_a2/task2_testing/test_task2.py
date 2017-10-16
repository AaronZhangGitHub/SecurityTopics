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
    for file in filesToTest:
        passAllCases = True
        studentOnyen = file.split('_')
        print(studentOnyen[1])
        for test in tests:
            arg1 = test['inputArg1']
            arg2 = test['inputArg2']
            outputVal = os.popen('python3 ./StudentFiles_task2/%s %s %s' % (file,arg1,arg2)).read().rstrip()
            expectedOutput = test['output']
            if outputVal!=expectedOutput:
                passAllCases = False
                break
        print(passAllCases)

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
