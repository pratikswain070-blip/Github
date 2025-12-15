# class InsuffiecientBalance(Exception):
#     def __init__(self):
#         super().__init__(
#             f"Insufficient balance"
#         )
# class ATMAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             raise InsuffiecientBalance()
#         self.balance-=amount
#         print(f"rupees {amount} withdrawn successfully")
#         print(f"remaining balance: {self.balance}")

# try:
#     account=ATMAccount(1000)
#     account.withdraw(100)
# except Exception as e:
#     print(e)
        
# class employee:
#     def __init__(self,name,empid):
#         self.name=input("enter the name:")
#         self.empid=int(input("enter the empid:"))
#     def show_details(self):
#         print("Name:",self.name)
#         print("EmpID:",self.empid)

# class manager(employee):
#     def __init__(self,name,empid,teamsize):
#         super().__init__(name,empid)
#         self.teamsize=int(input("enter the team size:"))
    
#     def show_d(self):
#         super().show_details()


# class developer(employee):
#     def __init__(self,name,empid,programming_language):
#         super().__init__(name,empid)
#         self.programming_language=input("enter the programming language:")
    
#     # def show_developer_info(self):
#     #     print("Programming Language:",self.programming_language)

# class intern(employee):
#     def __init__(self,name,empid,duration):
#         super().__init__(name,empid)
#         self.duration=int(input("enter the duration in months:"))

# m = manager("harsh",101,5)
# m.show_d()


n=int(input("enter the number:"))
for i in range(1,n+1):
    if i==n or i==1:
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")