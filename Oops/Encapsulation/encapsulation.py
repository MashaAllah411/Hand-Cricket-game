#Public access specifier

class Solution:
    def __init__(self,name,number,degree,stream,cgpa):
        self.name=name
        self.number=number
        self.degree=degree
        self.stream=stream
        self.cgpa=cgpa
        
    def Acess(self):
        print(self.name)
        print(self.number)
        print(self.degree)
        print(self.stream)
        print(self.cgpa)
        
        
c=Solution("Masha",9790,"B.E","CS",8.9)
#by calling directly
print(c.name)
#by calling by defining an func
c.Acess()


#Private access specifier "(_)""

class Company:
    def __init__(self,emp_name,emp_salary,emp_id):
        self.emp_name=emp_name
        self._emp_salary=emp_salary
        self.emp_id=emp_id
        
    def manager(self):
        return f"Salary of the employees is {self._emp_salary}"
        
    def access(self):
        print(f"Employee Name :{self.emp_name}")
        print(f"Employee ID :{self.emp_id}")
        
d=Company("Masha",25000,311020106030)\

d.access()

print(d.manager())

print(d._emp_salary)#Possible, but not recommended(protected)


#Protected Aceess Specifier "(__)"

class Bank:
    def __init__(self,user_name,user_contact,user_id,acc_balance):
        self.user_name=user_name
        self.user_contact=user_contact
        self.user_id=user_id
        self.__acc_balance=acc_balance
        
        
    def accessobj(self):
        print(f"User Name :{self.user_name}")
        print(f"User Contact :{self.user_contact}")
        print(f"User Id :{self.user_id}")
        
    def deposit(self,amount):
        if amount>0:
            self.__acc_balance+=amount
            return f"Deposited {amount} New Balance :{self.__acc_balance}"
        else:
            return "INvalid Deposit"
            
    def Withdrawmoney(self,amount):
        if amount <= self.__acc_balance:
            self.__acc_balance-=amount
            return f"Withdrawn {amount} Remaining Balance: {self.__acc_balance}"
        else:
            return "Enterd amount is greter then the bank balance"
            
    def Checkbalance(self):
        return f"Current Balance :{self.__acc_balance}"

#Taking input from User

user_name=input("Enter the User Name :")
user_contact=input("Enter the User Contact number :")
user_id=input("Enter the User ID :")
acc_balance=float(input("Enter the Amount :"))

#Calling the class
person=Bank(user_name,user_contact,user_id,acc_balance)

#Calling the object
person.accessobj()

#Giving Options TO Users
operation=input("Enter the Option :(Deposit/Withdraw/checkbalance) ")

#Based on the User requirements doing the opertion

if operation=="Deposit":
    amount = float(input("Enter the amount to deposit: "))
    print(person.deposit(amount))
elif operation=="Withdraw":
    amount = float(input("Enter the amount to withdraw: "))
    print(person.Withdrawmoney(amount))
elif operation=="checkbalance":
    print(person.Checkbalance())
