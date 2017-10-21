import itertools , string, random
from itertools import product
from string import ascii_lowercase, digits
import hashlib

m = hashlib.sha256()
l = hashlib.sha256()
values = []
strings = []
count2 = 0
count3 =0
hex1 = 0

for n in range(0,30):
	string2 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
	strings.append(string2)
	l.update(string2.encode("UTF-8"))
	hex2 = l.hexdigest()
	values.append(hex2)
	l=0
	l = hashlib.sha256()

#for n in range(1,20):
for x in map(''.join, itertools.product(digits+ascii_lowercase, repeat = 8)):
		count3 +=1
		m.update(x.encode("UTF-8"))
		hex1 = m.hexdigest()
		for v in values:
			hex2 = values[count2]
			for y in range(0,6):  
				if (hex1[y] != hex2[y]):
					break
				if (hex1[y] == hex2[y]):
					if(y==5):
						print (x, strings[count2], hex1)
						exit()
			count2 +=1
			m = 0
			m = hashlib.sha256()
		count2 =0
	

		

		

