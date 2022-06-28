import base64
#----------------
import os
os.system('clear')
#----------------
txt=input('TXT:  ')

has1=base64.a85decode(txt)

print(has1)
