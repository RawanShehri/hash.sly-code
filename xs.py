import hashlib 

import python

import os


#--------------
os.system('clear')
#---------------

o=str(input("your Text -> "))

g=hashlib.sha1(b'{}').format(o).hexdigest()

ft=len(g)

print(f"number of symbols -> {ft}")

print(f"your hash -> {g}")
