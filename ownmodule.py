import module as modu 
"""
r = modu.greeting("Pratik!")

print(r)

print(modu.dic)
print(modu.list1)
print(modu.tuple1)
print(modu.set1)

try:
 print(x)
except:
 print("An error occurred")


try:
 x=10 
 print(x)
except:
 print("An error occurred")

try:
 y = 10 
 print(y )
except NameError:
 print("Variable x is not defined")
except:
    print("An error occurred")

try:
 y = 70
 print(y )
except:
 print("Variable is not defined")
else:
    print("An error not occurred")


try:
 x = ps
 print(x )
except:
 print("Variable is not defined")
finally:
    print("The 'try except' is finished")
 """
try:
   f=open ("demofile.txt","w")
   try:
     f.write("My Name is Pratik Swain")
   except:
      print("Something went wrong when writing to the file")
   finally:
      f.close()
except:
    print("Something went wrong when opening the file")