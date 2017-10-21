
import sys, hashlib, itertools, string
from itertools import product
from string import ascii_lowercase

inputHash = (sys.argv[1])[:6]

for combo in product(ascii_lowercase+string.digits, repeat=7):

    hash = hashlib.sha256()
    stringValue = ''.join(combo)
    hash.update(stringValue.encode('utf-8'))
    if hash.hexdigest()[:6] == inputHash:
        print(stringValue)
        break
