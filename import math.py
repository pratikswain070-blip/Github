"""
import math
print(int(math.pi))
math.sqrt(25)
print(math.sqrt(25))
print(math.pow(2,3))

print(math.ceil(4.3))
print(math.floor(4.9))

import datetime
now = datetime.datetime.now()
print(now)
today = datetime.date.today()
print(today)

d=datetime.date(2025,1,12)
print(d.strftime("%y-%d-%m"))
"""
import random
random.random()
print(random.random())
random.randint(1,10)
print(random.randint(1,10))
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

cards=[1,2,3,4,5]
random.shuffle(cards)
print(cards)