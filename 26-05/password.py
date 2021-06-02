import re

txt=input("Enter a password")

#Check if the string has any characters between a and n:

small = re.findall("[a-z]", txt)
caps = re.findall("[A-Z]", txt)
no = re.findall("[0-9]", txt)
specl = re.findall("[$#@]", txt)
length=len(txt)
l=False
if(length>=6 and length<=16):
    l=True

if small and caps and no and specl and l:
    print("valid")
else:
    print("invalid")
