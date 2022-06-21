import hashlib 

#--------------

o=input("your Text -> ")

g=hashlib.sha1(f"b"{o} "").hexdigest()

print(f"your hash -> {g}"
