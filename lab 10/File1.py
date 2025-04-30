#to create a csv file and open it in MS Excel
f = open("C:\\Users\\24BCP067\\Desktop\\DATA.csv",'a+')
rlno = input("Enter  roll no or enter to end")
while rlno:
    nm = input("Entr name")
    cp, maths, ch = input("Enter computer, maths and chem marks:").split()
    f.write(rlno+","+nm+","+cp+","+maths+","+ch+","+'\n')
    rlno = input("Enter  roll no or enter to end")
f.close()
