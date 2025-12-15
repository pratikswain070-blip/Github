"""
class students:
    name="Pratik"
    age=18
    rollno=184
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)

s1=students()
s1.display()
s2=students()
s2.name="Rahul"
s2.age=19
s2.rollno=185
s2.display()
s3=students()
s3.name="ankit"
s3.age=17
s3.rollno=1234
s3.display()
"""

class employees:
    Name=""
    Companyname=""
    Salary=0
    exp=0

    def display(self):
      
        self.Companyname=input("enter the company name:")
       
        self.Salary=int(input("enter the salary:"))
        
        self.exp=int(input("enter the experience:"))

        self.Name=input("enter the name:")

        print("Name:" ,self.Name)
        print("Companyname:" ,self.Companyname)
        print("Salary:",self.Salary )
        print("exp:",self.exp)

e1=employees()
e1.display()
print("---------------------Employee------------------------------")
e2=employees()
e2.display()







print("Choose your employee type:")
print("1. Manager")
print("2. Developer")
print("3. Intern")
choice = input("Enter the choice number:")
name=input("Enter the employee name:")
empid=int(input("Enter the employee ID:"))

if choice == '1':
    team_size = int(input("Enter the team size:"))
    emp=Manager(name, empid, team_size)
elif choice == '2':
    lan=input("Enter the programming language:")
    emp=Developer(name, empid, lan)
elif choice == '3':
    duration = int(input("Enter the duration in months:"))
    emp=Intern(name, empid, duration)
else:
    print("Invalid choice!")
    emp=None

print("\nEmployee Details:")
emp.show_details()
