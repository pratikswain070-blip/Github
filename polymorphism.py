# class calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
# calc = calculator()
# print(calc.add(2, 3)) #this will raise an error 
# print(calc.add(2, 3, 4))

# class animal:
#     def sound(self):
#         print("Animal makes a sound")
# class dog(animal):    
#     def sound(self):
#         print("Dog barks")
# class cat(animal):
#     def sound(self):
#         print("Cat meows")

# a=animal()
# a.sound()
# d=dog()
# d.sound()
# c=cat()
# c.sound()

# class calculator:
#     def add(self,a,b=0,c=0):
#         return a+b+c
# cal=calculator()
# print(cal.add(2))
# print(cal.add(2,3))
# print(cal.add(2,3,4))


# class calculator:
#     def add(self,a,b=0,c=0,d=0,e=0):
#         return a+b+c+d+e
# cal=calculator()
# print(cal.add(2))
# print(cal.add(2,3))
# print(cal.add(2,3,4))
# print(cal.add(2,3,4,5))
# print(cal.add(2,3,4,5,6))


# class calculator:
#     def add(self,*args):
#         return sum(args)
# cal=calculator()
# print(cal.add(2))
# print(cal.add(2,3))
# print(cal.add(2,3,4))
# print(cal.add(2,3,4,5))
# print(cal.add(2,3,4,5,6))

# class calculator:
#     def add(self, a,b,c,d):
#         return a + b + c + d
#     a=int(input("enter first number:"))
#     b=int(input("enter second number:"))
#     c=int(input("enter third number:"))
#     d=int(input("enter fourth number:"))
# cal=calculator()
# if(cal.a<0 or cal.b<0 or cal.c<0 or cal.d<0):
#      print("Negative numbers are not allowed")
# # elif len(cal.a,cal.b,cal.c,cal.d)<4:
# #         print("Please enter four numbers")
# # elif len(cal.a,cal.b,cal.c,cal.d)>4:
# #      print("Please enter only four numbers")        
      
# else:
#      print("Sum is:",cal.add(cal.a,cal.b,cal.c,cal.d))


# class calculator:
#      def add(self, *args):
#       if len(args)==2:
#             print("Adding two numbers")
#             return args[0] + args[1]
#       elif len(args)==3:
#             print("Adding three numbers")
#             return args[0] + args[1] + args[2]
#       elif len(args)==4:
#             print("Adding four numbers")
#             return args[0] + args[1] + args[2] + args[3]
#       else:
#        return "Please provide 2, 3, or 4 numbers only"
      
# cal = calculator()
# print(cal.add(int(input("Enter first number: ")), int(input("Enter second number: "))))
# print(cal.add(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))))
# print(cal.add(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")), int(input("Enter fourth number: "))))
# print(cal.add(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")), int(input("Enter fourth number: ")),int(input("Enter fifth number: "))))


class calculator:
    def add(self,a,b):
     if isinstance(a, int) and isinstance(b, int):
        return a+b
     elif isinstance(a, str) and isinstance(b, str):
        return a+" "+b
     else:
        return "Invalid input types"
cal=calculator()
print(cal.add(2,3))
print(cal.add("Hello","World"))
        

