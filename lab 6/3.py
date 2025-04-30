from datetime import date
date1 = (30,11,2006)
date2 = (22,5,2002)

obj1=date(date1[2],date1[1],date1[0])
obj2=date(date2[2],date2[1],date2[0])

difference = (obj2-obj1).days

print("Numbers of days between the 2 dates:",difference)
