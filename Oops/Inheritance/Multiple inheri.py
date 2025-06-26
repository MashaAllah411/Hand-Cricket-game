class Father:
    def details_dad(self,dad_name,dad_age,dad_occupation,salary):
        self.dad_name=dad_name
        self.dad_age=dad_age
        self.dad_occupation=dad_occupation
        self.salary=salary
        
    def access(self):
        print(f"Father's Name :{self.dad_name}")
        print(f"Father's Age :{self.dad_age}")
        print(f"Father's Occupation :{self.dad_occupation}")
        print(f"Father's Salary :{self.salary}")

class Mother:
    def details_mom(self,mom_name,mom_age,mom_occupation):
        self.mom_name=mom_name
        self.mom_age=mom_age
        self.mom_occupation=mom_occupation
        
    def accessobj(self):
        print(f"Mother's Name :{self.mom_name}")
        print(f"Mother's Age :{self.mom_age}")
        print(f"Mother's Occupation :{self.mom_occupation}")
        
class Son(Father,Mother):
    def student(self,name,age,class_name,rollno,mom_name,mom_age,mom_occupation,dad_name,dad_age,dad_occupation,salary):
        
        super().details_dad(dad_name,dad_age,dad_occupation,salary)
        
        Mother.details_mom(self,mom_name,mom_age,mom_occupation)
        self.name=name
        self.age=age
        self.class_name=class_name
        self.rollno=rollno
        
    def result(self):
        print("Fathers Details")
        print("-----------------------------")
        super().access()
        print("-----------------------------")
        print("Mother Details")
        print("-----------------------------")
        self.accessobj()
        print("-----------------------------")
        print("Son details")
        print("-----------------------------")
        print(f"Son's Name :{self.name}")
        print(f"Son's age :{self.age}")
        print(f"Class Name :{self.class_name}")
        print(f"Rollno :{self.rollno}")
        
s=Son()
s.student(name="Masha", age=15, class_name="10th", rollno=25,
    mom_name="fathima", mom_age=40, mom_occupation="Teacher",
    dad_name="Abdul", dad_age=45, dad_occupation="Engineer", salary=90000)
s.result()
        
        
        
    
        
        


