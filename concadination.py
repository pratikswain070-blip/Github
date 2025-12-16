
a = ["apple","cherry","mango","banana"]
print(a[1:4])
print(a[:2])
print(a[2:])


fruits=["apple","cherry","mango","banana"]
print(fruits)
#fruits[2]="kivi"
#fruits.insert(2,"orange")
#fruits.extend(["hi ", "kaissa"])
fruits += ["hi ", "kaissa"]
print(fruits)
#fruits.remove("hi ")
fruits.pop(1)
print(fruits)


a=["student","college"]
b=["student","college"]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)


fruits=["a","c","b","a","c","b"]
while "b" in fruits:
    fruits.remove("b")
print(fruits)

a=[1,2,3,4,5,6,7,8]
del a[0:4]
print(a)
del a[3:4]
print(a)
del a[2:6]
print(a)



colors = ("red", "green", "blue")
(r, g, b) = colors
print(r) 
print(g)
print(len(colors))
print(type(colors))


a = ("apple")
print(a)
print(type(a))
b=("apple",)
print(b)
print(type(b))


t=()
print(t)
print(type(t))


r=tuple([1,2,3,4,5,6])
print(r)
print(type(r))
 
q=tuple(("apple"))
print(q)
w=tuple(("apple",))
print(w)
e=tuple(["apple"])
print(e)


fruits=("apple","cherry","mango","banana","kiwi","orange","cheery")
print(fruits[-4:-1])

t=("a","b","c","d","e")
print(t[2:4])
print(t[-4:-1])


t=("a","b","c","d","e")
if "f" in t:
    print("yes,'a' is in tuple t")
else:
    print("no,'f' is not in tuple t")

f=["apple","cherry","mango","banana"]
f[2]="kiwi"
print(f)

g=("apple","cherry","mango","banana")
u=list(g)
u[2]="kiwi"
g=tuple(u)
print(g)

f=("apple","cherry","mango","banana")
x=list(f)
x.insert(2,"kiwi")
f=tuple(x)
print(f) 


f=("apple","cherry","mango","banana")
x=list(f)
x.extend(["kiwi","papaya","orange"])
f=tuple(x)
print(f)


f=("apple","cherry","mango","banana")
x=list(f)
x.remove("apple")
f=tuple(x)
print(a)

t=("a","b","c","d","e")
(*x,y,z)=t
print(x)
(x,*y,z)=t
print(y)
(x,y,*z)=t
print(z