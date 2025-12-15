class bank:
    def __init__(self, acc_holder,ac_name,balance):
        self.acc_holder=acc_holder
        self.ac_name=ac_name

        self.__balance=balance
    def get_balance(self):
            return self.__balance
    def deposit(self,amount):
         if amount>0:
              self.__balance+=amount
              print(f"Deposited: {amount} successfully")
         else:
              print("Invalid amount. Deposit failed.")
    def withdraw(self,amount):
            if amount<=0:
                  print("Invalid amount. Withdrawal failed.")
            elif amount>self.__balance:
                    print("Insufficient balance. Withdrawal failed.")
            else:
                    self.__balance-=amount
                    print(f"Withdrew: {amount} successfully")
    def show_account(self):
            print("\n--------Account details--------")
            print(f"Account Holder:",self.acc_holder) 
            print(f"Account Name:",self.ac_name)
            print(f"Balance:",self.__balance)

name=input("enter the account holder name:")
ac_name=input("enter the account name:")
balance=float(input("enter the balance:"))
acc=bank(name,ac_name,balance)
acc.show_account()

print("\n======Bank Menu======")
print("1. Deposit")
print("2. Withdraw")
print("3. Show Balance")
print("4. Exit")
while True:
    choice=input("Enter your choice (1-4):")
    if choice=='1':
        amount=float(input("Enter amount to deposit:"))
        acc.deposit(amount)
    elif choice=='2':
        amount=float(input("Enter amount to withdraw:"))
        acc.withdraw(amount)
    elif choice=='3':
        print(f"Current Balance: {acc.get_balance()}")
    elif choice=='4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
      