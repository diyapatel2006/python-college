Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: C:/Users/lab/Desktop/DIYA PATEL/studentdata.py =====================
Enter Roll No.[Enter to end.]24BCP016
Enter Name,Marks of cp II,Maths and Chemistry:Rutvi
Traceback (most recent call last):
  File "C:/Users/lab/Desktop/DIYA PATEL/studentdata.py", line 4, in <module>
    nm,cp,maths,ch=input("Enter Name,Marks of cp II,Maths and Chemistry:").split()
ValueError: not enough values to unpack (expected 4, got 1)

====================== RESTART: C:/Users/lab/Desktop/DIYA PATEL/studentdata.py =====================
Enter Roll No.[Enter to end.]16
Enter Name,Marks of cp II,Maths and Chemistry:rutvi 21 19 17
Enter Roll No.[Enter to end.]

========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
16,rutvi,21,19,17


========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
Traceback (most recent call last):
  File "C:/Users/lab/Desktop/DIYA PATEL/read.py", line 1, in <module>
    f=open("C:\\Users\\lab\\Desktop\\studentdata")  #default mode is read
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\lab\\Desktop\\studentdata'

========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
Traceback (most recent call last):
  File "C:/Users/lab/Desktop/DIYA PATEL/read.py", line 1, in <module>
    f=open("C:\\Users\\lab\\Desktop\\studentsdata")  #default mode is read
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\lab\\Desktop\\studentsdata'

========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
Roll No.,Name,CPII,Maths,Chemistry
6,netri joshi,18,21,21
41,Diya patel,16,17,17
37,Happy,16,19,19


====================== RESTART: C:/Users/lab/Desktop/DIYA PATEL/studentdata.py =====================
Enter Roll No.[Enter to end.]16
Enter Name,Marks of cp II,Maths and Chemistry:rutvi 21 19 17
Enter Roll No.[Enter to end.]

========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
Roll No.,Name,CPII,Maths,Chemistry
6,netri joshi,18,21,21
41,Diya patel,16,17,17
37,Happy,16,19,19
16,rutvi,21,19,17

>>> 
========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
['Roll No.,Name,CPII,Maths,Chemistry\n', '6,netri joshi,18,21,21\n', '41,Diya patel,16,17,17\n', '37,Happy,16,19,19\n', '16,rutvi,21,19,17\n']
>>> 
========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
['Roll No.,Name,CPII,Maths,Chemistry\n']
>>> 
========================= RESTART: C:/Users/lab/Desktop/DIYA PATEL/read.py =========================
Roll No.,Name,CPII,Maths,Chemistry

6,netri joshi,18,21,21

41,Diya patel,16,17,17

>>> 
==================== RESTART: C:/Users/lab/Desktop/DIYA PATEL/csv/question 2.py ====================
{'Roll No.': ['6', '41', '37', '16'], 'Name': ['netri joshi', 'Diya patel', 'Happy', 'rutvi'], 'CPII': ['18', '16', '16', '21'], 'Maths': ['21', '17', '19', '19'], 'Chemistry': ['21', '17', '19', '17']}
