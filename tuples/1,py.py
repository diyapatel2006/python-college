# question - 1
"""
name=[("Diya","jil",),("Saakshi"),("Dhruvi","Hetvi")]

boys_count=0
girls_count=0

for ele in name:
    if isinstance(ele,tuple):
        boys_count +=1
    else:
        girls_count +=1
        
print("Number of boys:",boys_count)
print("Number of girls:",girls_count)
#jyare apde diya,jil jode xyz lakye che tyare output ma number of boys ma 2 ave che istead of 3(or any other logic behind it)
"""

#question 2
"""
students=[(41,"Diya",18),(98,"Jil",17),(163,"Hetvi",19)]

rolno=[]
name=[]
age=[]

for student in students:
    rolno.append(student[0])
    name.append(student[1])
    age.append(student[2])

print("Roll no:",rolno)
print("Name:",name)
print("Age:",age)
"""

#question 3
"""
from datetime import date
date1 = (30,11,2006)
date2 = (22,5,2002)

obj1=date(date1[2],date1[1],date1[0])
obj2=date(date2[2],date2[1],date2[0])

difference = (obj2-obj1).days

print("Numbers of days between the 2 dates:",difference)
"""

#question 4
"""
items=[("Burger",5),("Pizza",86),("Pasta",78),("salad",97)]

sorted=sorted(items,reverse=True)

print("Sorted food items by price(Descending):",sorted)
"""

#question 5
"""
list=[(),("Diya",18),("jil",17),(),("Hetvi"),()]

l1=[ele for ele in list if ele]
print(l1)

lst=[(),("Diya",18),("jil",17),(),("Hetv"),()]
for ele in lst:
    if(len(i)==0):
        lst.remove(i)
        print(lst)
        # check this question
"""

#question 6
#check the concept
"""
tpl=(1,2,3,4)

lst=list(tpl)
lst[2]=99
tpl2=tuple(lst)

print("Modified tuple:",tpl2)
"""

#question 7
"""
tpl=(67,75,85,26)
temp=list(tpl)

temp.remove(67)
tpl=tuple(temp)

print(tpl)
"""
#Another method
"""
tpl=(100,200,300,400)

lst=list(tpl)
del(lst[2])
tpl2=tuple(lst)

print("Modified tuple:",tpl2)
"""
#output of the code
lst=[('x','y','z'),40,50,60]
a=lst[0]
print(a)
































