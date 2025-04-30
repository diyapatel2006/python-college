def obtlen(s):
    if len(s)==0:
        return 0
    if s[0]==' ':
        return obtlen(s[1:])
    else:
        return 1+obtlen(s[1:])
print(len(diya patel))
