import sys

print (bin(int(sys.argv[2],16) ^ int(sys.argv[1],16) ).count('1'))
