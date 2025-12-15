""" 
x=None

if x is None:
    raise NameError("value error")
    

x=None
if x<0:
    raise ValueError("Negative value error")
elif x is None:
    raise TypeError("value error")

x="Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
 """
f=open("/Users/pratikswain/Desktop/python/xyz.txt")
print(f.read())

with open("xyz.txt","w") as f:
    f.write("Hello World")
    
with open("xyz.txt","r") as f:
    print(f.read())

with open("xyz.txt","a") as f:
    f.write("Welcome to Python programming")

with open("xyz.txt","r") as f:
    print(f.read())

 