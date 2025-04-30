class Polygon:
    def __init__(self,n,d):
        self.sides=n
        self.length=d
    def perimeter(self):
        p=self.sides*self.length
        return p
    def area(self):
        area=self.length**self.sides
        return area
pentagon=Polygon(5,2)
print("perimeter:",pentagon.perimeter()," area:",pentagon.area())
