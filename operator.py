""" 
from ast import literal_eval

a=input("Enter first number: ")
b=input("Enter second number: ")
print("Addition", a+b)

a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))

print("subtraction:",a-b)

a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))

print("mutiplication:" , a*b)

a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))


print("Division:", a/b)

a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))

print("Exponentiation:" , a**b)
a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))

print("Modulus:", a % b)

a=literal_eval(input("Enter first number: "))
b=literal_eval(input("Enter second number: "))
print("Floor division:", a//b)


e=a*b
f=a/b
g=a**b
i=a%b
j=a//b

print("Addition:",c)
print("Subtraction:",d)
print("Multiplication:",e)
print("Division:",f)
print("Exponentiation:",g)
print("Modulus:",i)
print("Floor Division:",j)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))    
c=input("Enter operator (+, -, *, /, **, %, //): ")
print("Result:", c, end=" ")


x=int(input("Enter number: "))
print(f"the initial value of x = {x}")
x += 5
print(f"After x += 5: {x}")
x-=3
print(f"After x -= 3: {x}")
x*=2
print(f"After x *= 2: {x}")
x/=4
print(f"after x /=4: {x}")
x%=3
print(f"After x %= 3: {x}")
x**=2
print(f"after x **=2: {x}")
x//=5
print(f"After x//=5 : {x}")



a= eval(input("Enter first number: "))
b= eval(input("Enter second number: "))
print("a==b:",  (a==b))
print("a!=b:", (a!=b))
print("a>b :", (a>b))
print("a<b :", (a<b))
print("a>=b :", (a>=b))
print("a<=b :", (a<=b))




a = input("Enter the first value:")
b = input("Enter the second value:")

print("a and b : " , (a and b) )
print("a or b :" , (a or b))
print("not a :" , (not a) )
""" 
a = bool(int(input("Enter first value (0 for False, any nonzero for True): ")))
b = bool(int(input("Enter second value (0 for False, any nonzero for True): ")))

print("Results of Logical Operations:")
print(f"a and b -> {a and b}")
print(f"a or b -> {a or b}")
print(f"not a -> {not a}")
print(f"not b -> {not b}")