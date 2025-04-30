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
