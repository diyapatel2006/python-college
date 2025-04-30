def count_alpha_digits(s):
     d={}
     alpha=0
     digit=0
     for i in s:
         if i not in d:
             d[i] = 1
         else:
             d[i] = d[i] + 1
         if i.isalpha():
             alpha+=1
         if i.isdigit():
             digit+=1
     print(d)
     print("Alhpabets:",alpha,"Digits:",digit)
count_alpha_digits(input("Enter a string"))
