# Base class
class Person:
    def info(self):
        print("This is a person.")

# First level
class Father(Person):
    def father_info(self):
        print("Father's info.")

class Mother:
    def mother_info(self):
        print("Mother's info.")

# Hybrid: inherits from Father (who inherits Person) and Mother
class Child(Father, Mother):
    def child_info(self):
        print("Child's info.")


c = Child()
c.info()      
c.father_info() 
c.mother_info() 
c.child_info()   
