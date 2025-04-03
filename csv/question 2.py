# question 2
f=open("C:\\Users\\lab\\Desktop\\studentsdata.csv")
All_Data=f.readlines()
Filter=[lines.strip().split(',')for lines in All_Data]
Empty_Dictionary={}
columns=len(Filter[0])
for i in range(columns):
    Empty_Dictionary[Filter[0][i]]=[lines[i] for lines in Filter[1:]]
f.close()
print(Empty_Dictionary)
    
