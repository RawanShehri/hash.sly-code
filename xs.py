import hashlib 

#--------------

o=input("your Text -> ")

g=hashlib.sha1(b"{}".format(o).hexdigest()

print(f"your hash -> {g}")
