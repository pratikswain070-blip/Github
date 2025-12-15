"""
square= lambda x: x*x*x
print(square(5))

add= lambda a,b: a+b
print(add(10,20))

nums=[1,2,3,4,]
result= list(map(lambda x: x*2, nums))
print(result)

num=[2,4,6,8]
result= list(map(lambda x: x//2, num))
print(result)

n=[9,10,12,14]
even=list(filter(lambda x: x%2==0, n))
print(even)

s=[("Pratik",25),("John",30)]
s.sort(key=lambda x: x[1], reverse=False)
print(s)

def decorator(func):
    def wrapper():
        func()
        print("Before executing the function")
        func()
        print("After executing the function")
        func()
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()

""" 
import time

def simple_timer(func):
    def wrapper():
        print(f"{func.__name__} started")
        start = time.time()
        result = func()
        duration = time.time() - start
        print(f"{func.__name__} ended")

        return result
    return wrapper

@simple_timer
def process_data():
    time.sleep(2)

@simple_timer
def generate_report():
    time.sleep(1)

@simple_timer
def upload_file():
    time.sleep(3)

if "name==main":
    process_data()
    generate_report()
    upload_file()

