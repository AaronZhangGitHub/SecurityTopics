import json
HAMMING_GRADES = "./hamming_grades.json"
PREIMAGE_GRADES = "./preimage_grades.json"
COLLISION_GRADES = "./collision_grades.json"
def somethings():
    with open(HAMMING_GRADES) as inFile:
        jsonData = json.load(inFile)
    count1 = 0
    sum1 = 0
    count_no_zero_val = 0
    sum_no_zero_val = 0
    for key, value in jsonData.items():
        if value!=0:
            count_no_zero_val+=1
            sum_no_zero_val+=value
        count1+=1
        print(key,value*100)
        sum1+=value*100
    print(count1,sum1/count1)
    print(count_no_zero_val, sum_no_zero_val)


import itertools
f1 = open(HAMMING_GRADES)
f2 = open(PREIMAGE_GRADES)
for x, y in zip(f1, f2):
    print ("%s %s" % (x.rstrip(), y.rstrip()))
