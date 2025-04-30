#pass fail and grade
s1 = float(input("Enter marks of subject 1:"))
s2 = float(input("Enter marks of subject 2:"))
s3 = float(input("Enter marks of subject 3:"))
t=s1+s2+s3
avg = t/3
if s1<40 or s2<40 or s3<40:
    print("Fail!")
else:
    print("Pass!")
print("Total:",t)
print("Average:",avg)
print("Subject 1:")
if s1<40:
    print("F")
elif s1<45:
    print("P")
elif s1<50:
    print("C")
elif s1<55:
    print("B")
elif s1<60:
    print("B+")
elif s1<70:
    print("A")
elif s1<80:
    print("A+")
else:
    print("O")
print("Subject 2:")
if s2<40:
    print("F")
elif s2<45:
    print("P")
elif s2<50:
    print("C")
elif s2<55:
    print("B")
elif s2<60:
    print("B+")
elif s2<70:
    print("A")
elif s2<80:
    print("A+")
else:
    print("O")
print("Subject 3:")
if s3<40:
    print("F")
elif s3<45:
    print("P")
elif s3<50:
    print("C")
elif s3<55:
    print("B")
elif s3<60:
    print("B+")
elif s3<70:
    print("A")
elif s3<80:
    print("A+")
else:     
    print("O")
