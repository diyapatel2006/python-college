class number:
    
    def set_num(self,n):
        
        self.num=n
        
    def get_num(self):
        
        return self.num
    
    def __init__(self):
        
        self.num=0
        
    def print_num(self):
        
        print(self.num)
        
    def isnegative(self):
        
        if self.num<0:
            
            return "-ve"

        elif self.num>0:
            
            return "+ve"
        
        else:
            
            return "zero"
        
    def isdivisibleby(self,n):
        
         if self.num % n==0:
             
             return "yes,divisible"
            
         else:
             
             return "no, not dividible"
            
    def abs_val(self):
        
         if self.num<0:
             
             return -(self.num)

         else:
             
             return self.num
            
    def __del__(self):
        
         print("deleting object:",str(self))
         
         
x=int(input("Enter a number:"))

a=number()

a.set_num(x)

b=a.get_num()

print("you entered value:",b)

a.print_num()

print(a.isnegative())

print(a.isdivisibleby(10))

print("Absolute Value:",a.abs_val())
N
a=None






         

         
        
