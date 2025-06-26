class Solution():
    def biodata1(self,name,age,class_name,roll_number):
        self.name=name
        self.age=age
        self.class_name=class_name
        self.roll_number=roll_number

    def accessobj(self):
        print(f"Name :{self.name}")
        print(f"age :{self.age}")
        print(self.class_name)
        print(self.roll_number)

class student(Solution):
    def biodata2(self,name,age,class_name,roll_number,tamil,english,maths,science,social):
        super().biodata1(name,age,class_name,roll_number)
        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.social=social

    def Accessobj(self):
        super().accessobj()
        print(f"Tamil Mark :{self.tamil}")
        print(f"English Mark :{self.english}")
        print(f"Maths Mark :{self.maths}")
        print(f"Science Mark :{self.science}")
        print(f"Social Mark :{self.social}")


name = input("Enter Name: ")
age = int(input("Enter Age: "))
number = input("Enter Phone Number: ")
class_name = (input("Enter Class: "))

print("\nEnter Marks (out of 100):")
english = int(input("English: "))
tamil = int(input("Tamil: "))
maths = int(input("Maths: "))
science = int(input("Science: "))
social = int(input("Social: "))

obj=student()
obj.biodata2(name,age,class_name,number,tamil,english,maths,science,social)
obj.Accessobj()

