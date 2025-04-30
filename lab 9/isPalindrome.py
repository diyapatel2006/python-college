def isPalindrome(s):
     if s.lower()==s.lower()[::-1]:
         return True
     else:
         return False
s = input("Enter a string")
print("Is palindrome:",isPalindrome(s))
