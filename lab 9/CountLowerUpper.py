def count_lower_upper(s):
     d={}
     for ch in s:
         if ch not in d:
             if ch.islower():
                 d[ch] = s.count(ch)
             if ch.isupper():
                 d[ch] = s.count(ch)
     print(d)
s = input("Enter a string")
count_lower_upper(s)
