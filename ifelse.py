# p=input("enter the post:")
# if("pratik" in p.lower()):
#     print("yes")
# else:
#     print("no")

# for i in range(4):
#     print("printing")
#     if i==2:
#         continue
#     print(i)

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")
"""
n=int(input("enter the number:"))
for i in range(1,11):
    print(f"{n}x{i}:",n*i)


n=int(input("enter the number:"))
for i in range(1,11):
    print(f"{n}x{11-i}:",n*(11-i))
"""
def goodbye(name,age):
    print("goodbye", name,age)
goodbye("pratik", 25)