f=open("sample.txt",'r')
x=input("Enter word to search in file")
l=f.readlines()
c=0
for s in l:
    k=s.split(' ')
    for st in k:
        if("\n" in st):
            st=st[:-1]
        if(st==x):
            c+=1
print("No of occurances of "+x+" in file : "+str(c))
       
