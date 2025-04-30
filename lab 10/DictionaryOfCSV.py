f = open("C:\\Users\\24BCP067\\Desktop\\DATA.csv")
data = f.readlines()
filt = [lines.split(",") for lines in data]
d={}
for i in range(len(filt[0])):
    d[filt[0][i]]=[lines[i] for lines in filt[1:]]
f.close()
print(d)
