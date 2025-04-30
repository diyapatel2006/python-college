class Shape:
    
    def __init__(self,name,dimensions):
        self.type=name
        self.dimension=dimensions
    def SA(self):
        if self.type =="sphere":
                r=self.dimension
                SA=(4*3.14)*(r**2)
                return SA        
        if self.type == "cube":
                l=self.dimension
                SA=6*(l**2)
                return SA
        if self.type=="cuboid":
              l=self.dimension[0]
              b=self.dimension[1]
              h=self.dimension[2]
              
              SA=2*((l*h)+(h*b)+(b*l))
              return SA
    def volume(self):
        if self.type =="cube":
                l=self.dimension
                volume=l**3
                return volume
        if self.type =="sphere":
                r=self.dimension
                volume=((4*3.14)*(r**3))/3 
                return volume
        if self.type=="cuboid":
              d=self.dimension
              l=d[0]
              b=d[1]
              h=d[2]
              volume=l*h*b
              return volume
                      
    
c=Shape("sphere",1)
print(c.SA())
print(c.volume())
c2=Shape("cuboid",[1,1,2])
print(c2.volume())
print(c2.SA())
