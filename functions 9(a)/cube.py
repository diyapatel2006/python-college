#high order function
"""
def cube(n):
    return n*n*n
print(cube(10))

lst=[2,5,7,20,60,44]
l=map(cube,lst)
print(list(l))

tupl=(2,3,4,5,6,7,8)
y=map(cube,tupl)
print(tuple(y))

s={2,3,4,5,6,7,8}
x=map(cube,s)
print(set(x))

"""
'''

def fun(n1,n2):
    return n1*n2
lst=[2,5,7,20,60,44]
lst2=[5,6,7,8,9,10]
l=map(fun,lst,lst2)
print(list(l))

'''
'''
def upper(n):
    return n.upper()
str="My name is Diya"
a=map(upper,str)
print(tuple(a))

'''
x=lambda p,q:p*q
print(x(2,6))
lst=[2,3,4,5,6,7,8]
lst2=[8,7,6,5,4,3,2]
l=map(lst,lst2)
print(list(map(lambda n:n**3, [2,3,4,5,6])))







































