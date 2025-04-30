class Complex:
    def __init__(self,real,imaginary):
        self.rpart=real
        self.ipart=imaginary

    def __add__(self,other):
        z=Complex(self.rpart+other.rpart,self.ipart+other.ipart)
        return z
    
    def __sub__(self,other):
        z=Complex(self.rpart-other.rpart,self.ipart-other.ipart)
        return z
    
    def __mul__(self,other):
        z=Complex((self.rpart*other.rpart)-(self.ipart*other.ipart),(self.ipart*other.rpart)+(other.ipart*self.rpart))
        return z
    
c1=Complex(1.1,0.2)
c2=Complex(2.2,0.4)
c3=c1+c2
print(c3.rpart,c3.ipart)
c4=c1-c2
print(c4.rpart,c4.ipart)
c5=c1*c2
print(c5.rpart,c5.ipart)
