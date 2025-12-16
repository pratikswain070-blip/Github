a=input("Enter Student Name: ")
b=input("Enter Student Roll Number: ")
c=int(input("Enter Maths Marks: "))
d=int(input("Enter Science Marks: "))
e=int(input("Enter English Marks: "))
f=c + d + e
g= f / 3
g = round(g, 2)
print("------Report Card------")
print("Student Name:", a)
print("Student Roll Number:", b)
print("Total Marks:", f)
print("Average Marks:", g)
if c >= 33 and d >= 33 and e >= 33:
    print("Result: PASS")
else:
    print("Result: FAIL")