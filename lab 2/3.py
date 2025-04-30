#area or perimeter greater
l = float(input("Enter length"))
b = float(input("Enter breadth"))
a=l*b
p=2*(l+b)
print("Area:",a)
print("Perimeter:",p)
if a>p:
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")
