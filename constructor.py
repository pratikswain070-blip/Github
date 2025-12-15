"""
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = student("Pratik", 18)
s1.display()
s2 = student("Rahul", 19)
s2.display()

class student:
    def __init__(self, name, age):
        self.name=input("enter the name:")
        self.age=int(input("enter the age:"))
        print("Name:",self.name)
        print("Age:",self.age)
s1=student("","")

class student:
    def __init__(self,name,rollno,m1,m2,m3,percentage):
        self.name=input("enter the name:")
        self.rollno=int(input("enter the rollno:"))
        self.m1=int(input("enter the marks1:"))
        self.m2=int(input("enter the marks2:"))
        self.m3=int(input("enter the marks3:"))
        self.percentage=100*(self.m1+self.m2+self.m3)/300       
        self.show_report()
    def show_report(self):
        print("-------------------Report Card---------------------------")
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Marks:",self.m1, self.m2, self.m3)
        print("Percentage:",self.percentage)
s1=student("","",0,0,0,0)


class employees:
    def __init__(self,name,empid):
        self.name=input("enter the name:")
        self.empid=int(input("enter the empid:"))
        self.attendance=int(input("enter the attendance:"))
        self.mark_attendance()

    def mark_attendance(self):
        self.attendance+=1
        print(f"Attendance marked for {self.name}. Total attendance: {self.attendance}")
        self.show_details()

    def show_details(self):
        print("-------------------Employee Details---------------------------")
        print("Name:",self.name)
        print("EmpID:",self.empid)
        print("Attendance:",self.attendance)     
e1=employees("","")   

class person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Name:",self.name)
class student(person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
    def display(self):
        print("Roll No:",self.rollno)

s1=student("Pratik",184)
s1.show()
s1.display()
print("________")
p1=person("Rahul")
p1.show()


class employee:
    def __init__(self,name,empid):
        self.name=input("enter the name:")
        self.empid=int(input("enter the empid:"))
    def show_details(self):
        print("Name:",self.name)
        print("EmpID:",self.empid)

class manager(employee):
    def __init__(self,name,empid,teamsize):
        super().__init__(name,empid)
        self.teamsize=int(input("enter the team size:"))
class developer(employee):
    def __init__(self,name,empid,programming_language):
        super().__init__(name,empid)
        self.programming_language=input("enter the programming language:")
    
    # def show_developer_info(self):
    #     print("Programming Language:",self.programming_language)

class intern(employee):
    def __init__(self,name,empid,duration):
        super().__init__(name,empid)
        self.duration=int(input("enter the duration in months:"))

    # def show_intern_info(self):
    #     print("Role: Intern")
    #     print("Duration (months):",self.duration)

     
# print("-------Manager Details-------")
# m1=manager("","",int(input("enter the team size:")))
# m1.show_details()
# print("Team Size:",m1.teamsize)
# print("-------Developer Details-------")
# d1=developer("","",input("enter the programming language:"))
# d1.show_details()
# d1.show_developer_info()
# print("-------Intern Details-------")
# i1=intern("","",int(input("enter the duration in months:")))
# i1.show_details()
# i1.show_intern_info()

print("Choose your employee type:")
print("1. Manager")
print("2. Developer")
print("3. Intern")
choice = input("Enter the choice number:")
name=input("Enter the employee name:")
empid=int(input("Enter the employee ID:"))

if choice == '1':
    team_size = int(input("Enter the team size:"))
    emp=manager(name, empid, team_size)
elif choice == '2':
    lan=input("Enter the programming language:")
    emp=developer(name, empid, lan)
elif choice == '3':
    duration = int(input("Enter the duration in months:"))
    emp=intern(name, empid, duration)
else:
    print("Invalid choice!")
    emp=None

print("\nEmployee Details:")
emp.show_details()

if choice == '1':
    print("Team Size:", emp.teamsize)
elif choice == '2':
    print("Programming Language:", emp.programming_language)
elif choice == '3':
    print("Duration (months):", emp.duration)
"""




class employee:
    def __init__(self,name,empid):
        self.name=input("enter the name:")
        self.empid=int(input("enter the empid:"))
    def show_details(self):
        print("Name:",self.name)
        print("EmpID:",self.empid)

class manager(employee):
    def __init__(self,name,empid,teamsize):
        super().__init__(name,empid)
        self.teamsize=int(input("enter the team size:"))
class developer(employee):
    def __init__(self,name,empid,programming_language):
        super().__init__(name,empid)
        self.programming_language=input("enter the programming language:")
    
    # def show_developer_info(self):
    #     print("Programming Language:",self.programming_language)

class intern(employee):
    def __init__(self,name,empid,duration):
        super().__init__(name,empid)
        self.duration=int(input("enter the duration in months:"))

    # def show_intern_info(self):
    #     print("Role: Intern")
    #     print("Duration (months):",self.duration)

     
# print("-------Manager Details-------")
# m1=manager("","",int(input("enter the team size:")))
# m1.show_details()
# print("Team Size:",m1.teamsize)
# print("-------Developer Details-------")
# d1=developer("","",input("enter the programming language:"))
# d1.show_details()
# d1.show_developer_info()
# print("-------Intern Details-------")
# i1=intern("","",int(input("enter the duration in months:")))
# i1.show_details()
# i1.show_intern_info()

while True:
    print("\n==========Employee Menu+==========")
    print("1.Add Manager")
    print("2. Add Developer")
    print("3. Add Intern")
    print("4. Show Employee Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name=input("Enter the employee name:")
        empid=int(input("Enter the employee ID:"))
        team_size = int(input("Enter the team size:"))
        emp=manager(name, empid, team_size)
        employee.append(emp)
    elif choice == '2':
        name=input("Enter the employee name:")
        empid=int(input("Enter the employee ID:"))
        lan=input("Enter the programming language:")
        emp=developer(name, empid, lan)
        employee.append(emp)
    elif choice == '3':
        name=input("Enter the employee name:")
        empid=int(input("Enter the employee ID:"))
        duration = int(input("Enter the duration in months:"))
        emp=intern(name, empid, duration)
        employee.append(emp)
    elif choice == '4':
        print("\nEmployee Details:")
        for emp in employee:
            emp.show_details()
            if isinstance(emp, manager):
                print("Team Size:", emp.teamsize)
            elif isinstance(emp, developer):
                print("Programming Language:", emp.programming_language)
            elif isinstance(emp, intern):
                print("Duration (months):", emp.duration)
            print("---------------------------")
    elif choice == '5':
        print("Exiting the program.")
        break
    