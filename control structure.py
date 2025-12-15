"""
age=int(input("Enter your age: "))

if age>=18:
    print("You are an adult.")
elif age>=13:
    print("You are a Teenager.")
else:
    print("You are a child")

age=9
has_id=True

if age>=18:
    if has_id:
        print("You are allowed to enter the club.")
    else:
        print("You need to show your ID to enter the club.")
else:
    print("You are not allowed to enter the club.")
    
age=15
is_member=True

if age >=18 and (is_member or age >=21):
    print("You are allowed to enter the event.")
else:
    print("You are not allowed to enter the event.")
    

for i in range(5):
    print(i)

count = 1
while count < 5:
    print(count)
    count +=2
   
for i in range(8):
    if i == 6:
        break
    print(i)

for i in range(8):
    if i == 6:
        continue
    print(i)
     
for i in range(5):
    print("count:", i)

for num in range(3, 9):
    print("num:", num)
 
for num in range(2,10,3):
    print("odd:", num)
    
def greet():
    print("Hello")
greet()

def greet(name):
    print("Hello", name)
greet("Pratik")

def add(a, b):
    return a + b
result=add(3, 5)
print("Sum:", result)
 
def test():
    x=10
    print(x)
test()
 
y=20
def show():
    print(y)
show()
print(y)

x=5
def func():
    print("inside", x)
func()
x=10
print("outside", x)

x=5
if x > 3:
    if x < 10:
        x += 2
    else:
        x -=1
else:
    x=0
print(x)



for i in range(2, 10, 2):
  if i==6:
    break
  print(i, end=" ")
    """ 
s=0
for i in range(1,6):
    if i%2==0:
        continue
    s+=i
print(s)