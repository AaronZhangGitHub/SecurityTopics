
import sys, hashlib, itertools, string
from itertools import product
from string import ascii_lowercase

hash_dict = {}

for combo in product(ascii_lowercase+string.digits, repeat=7):

    hash = hashlib.sha256()
    stringValue = ''.join(combo)
    hash.update(stringValue.encode('utf-8'))
    k = hash.hexdigest()[:6]
    if k in hash_dict:
        print(stringValue + " " +  hash_dict[k])
        break
    else:
        hash_dict[k] = stringValue
