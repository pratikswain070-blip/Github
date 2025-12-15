"""
class employees:
    Name=""
    Companyname=""
    Salary=0
    exp=0

    def display(self):
      
        Company_Name = self.Companyname=input("enter the company name:")
       
        Employee_Salary = self.Salary=int(input("enter the salary:"))
        
        Employee_Experience = self.exp=int(input("enter the experience:"))

        Employee_Name = self.Name=input("enter the name:")

        print("Name:" ,Employee_Name)
        print("Companyname:" ,Company_Name)
        print("Salary:",Employee_Salary )
        print("exp:",Employee_Experience)

e1=employees()
e1.display()
print("---------------------Employee------------------------------")
e2=employees()
e2.display()

#. 2nd way of doing the same thing
class employees:
    Name=""
    Companyname=""
    Salary=0
    exp=0

    def display(self):
      
        e1.Name=input("enter the name:")
        e1.Companyname=input("enter the company name:")
        e1.Salary=int(input("enter the salary:"))
        e1.exp=int(input("enter the experience:"))

        print("Name:" ,e1.Name)
        print("Companyname:" ,e1.Companyname)
        print("Salary:",e1.Salary )
        print("exp:",e1.exp)

e1=employees()
e1.display()
print("---------------------Employee------------------------------")
e2=employees()
e2.display()
"""

# class student:
#     def __init__(self):
#         self.name="amit"
#         self.age=20
# s1=student()
# s2=student()

# s2.name="sumit"

# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)

class students:
    college="ABC"

    def __init__(self,name):
        self.name=name
s1=students("pratik")
s2=students("rahul")

print(s1.college)
print(s2.college)
students.college="XYZ"
print(s1.college)
print(s2.college)