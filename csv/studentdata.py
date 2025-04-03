f=open("C:\\Users\\lab\\Desktop\\studentsdata.csv","a+")
rlno=input("Enter Roll No.[Enter to end.]")
while rlno:
    nm,cp,maths,ch=input("Enter Name,Marks of cp II,Maths and Chemistry:").split()

    f.write(rlno+','+nm+','+cp+','+maths+','+ch+'\n')

    rlno=input("Enter Roll No.[Enter to end.]")
f.close()    

    
