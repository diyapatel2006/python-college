f=open("C:\\Users\\lab\\Desktop\\studentsdata.csv")#default mode is read
i=0
while(i<3):
    content = f.readline() #f.readlines means sabko string main karega
    print(content)
    i+=1
f.close()
    


