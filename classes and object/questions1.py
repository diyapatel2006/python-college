# question 1 -> complex number...
"""
class Complex1:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def addComplex(self,ob2):
        real1=self.real + ob2.real
        img1=self.img + ob2.img
        print("ans is",real1,'+j',img1)
    def __str__(self):
        return f'The complex number is {self.real} + j{self.img}'
    def __del__(self):
        print("deleting object")
        
cob1=Complex1(5,6)
cob2=Complex1(10,20)
print(cob1)
print(cob2)
cob1.addComplex(cob2)
"""

"""
class Complex1:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def addComplex(self,ob2):
        real1=self.real + ob2.real
        img1=self.img + ob2.img
        print("ans is in operation method",real1,'+j',img1)
    def __add__(self,ob2):
        real1=self.real + ob2.real
        img1=self.img + ob2.img
        print("ans is",real1,'+j',img1)
        
    def __str__(self):
        return f'The complex number is {self.real} + j{self.img}'
    def __del__(self):
        print("deleting object")
        
cob1=Complex1(5,6)
cob2=Complex1(10,20)
print(cob1)
print(cob2)
cob1.addComplex(cob2)
cob1+cob2
"""
class Complex1:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def addComplex(self,ob2):
        real1=self.real + ob2.real
        img1=self.img + ob2.img
       # print("ans is in operation method",real1,'+j',img1)
    def __add__(self,ob2):
        real1=self.real + ob2.real
        img1=self.img + ob2.img
        print("ans is",real1,'+j',img1)
        
    def __str__(self):
        return f'The complex number is {self.real} + j{self.img}'
    def __del__(self):
        print("deleting object")
        
cob1=Complex1(5,6)
cob2=Complex1(10,20)
print(cob1)
print(cob2)
cob1.addComplex(cob2)
cob1+cob2






























