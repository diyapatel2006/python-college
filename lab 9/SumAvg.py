def sum_avg(*args):
     s=0
     for i in args:
         s = s+i
     avg = s/5
     return s,avg
print(sum_avg(98,99,97,98,100))
