# Operator overloading is when you change the behavior of operators (+, -, *, etc.) 
# for user-defined objects using special methods like __add__, __sub__, etc.

class Numbers:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Numbers(self.x+other.x,self.y+other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
p1=Numbers(1,2)
p2=Numbers(2,4)
p3=p1+p2
print(p3)


# Compile-time polymorphism, also known as static polymorphism, 
# is a type of polymorphism where the method or function that will be executed is determined at compile time. 
# This typically happens through method overloading or operator overloading

#By using *args like packing
class Solution:
    def summ(self,*nums):
        result=0
        for i in nums:
            result+=i
        return result

c=Solution
print(c.summ(1,22,3))

#by using Default method
class Solution2:
    def summ(a,b=0,c=0):
        return a+b+c
    
d=Solution2
print(d.summ(2,3))