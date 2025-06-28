from abc import ABC, abstractmethod

#example 1
class Solution(ABC):
    def __init__(self,emp_name,emp_id,emp_contact):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_contact=emp_contact
        
    @abstractmethod
    def display_info(self):
        pass
    
class details(Solution):
    def display_info(self):
        print(f"Emp Name :{self.emp_name}")
        print(f"Emp id :{self.emp_id}")
        print(f"Emp Contact :{self.emp_contact}")
        
c=details("masha",21,979949677)
c.display_info()

#example 2
class Vehicle(ABC):
    def __init__(self,name,model):
        self.name=name
        self.model=model
        
    @abstractmethod
    def engine(self):
        pass
    
class car(Vehicle):
    def engine(self):
        return f"{self.name} was manufactured in the year of {self.model} model has started the engine by using key"
        
class bike(Vehicle):
    def engine(self):
        return f"{self.name} was intoduced in the year of {self.model} model has started the engine by using a key "
        

d=car("maruthi",2019)
print(d.engine())

f=bike("r15 M",2023)
print(f.engine())  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    