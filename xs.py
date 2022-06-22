import hashlib 

#--------------

o=str(input("your Text -> "))

g=hashlib.sha1(o).hexdigest()

ft=len(g)

print(f"number of symbols -> {ft}")

print(f"your hash -> {g}")
