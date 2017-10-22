import os



def iterThroughStudentFiles():
    STUDENT_FILES = "./student_submissions"
    studentDirectories = []
    for root, dirs, files in os.walk(STUDENT_FILES):
        studentDirectories = dirs
        break


    for studentDir in studentDirectories:
        submissionFolder = "%s/%s/Submission attachment(s)"%(STUDENT_FILES,studentDir)
        temp = os.listdir(submissionFolder)
        studentOnyen = studentDir[studentDir.find('(')+1:studentDir.find(')')]
        if(len(temp)==0):
            #students get 0
            print(studentOnyen)
        else:
            print(studentOnyen,temp)
iterThroughStudentFiles()
