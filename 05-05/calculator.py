class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
    def mod(self):
        return self.a%self.b
a,b=map(int,input("Enter two numbers sep by space").split(' '))
calc=calculator(a,b)
ch=1
while ch!=6:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Modulo\n6.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print("Sum of:",a,"and",b,"is",calc.add())
    elif ch==2:
        print("Difference of:",a,"and",b,"is",calc.sub())
    elif ch==3:
        print("Product of:",a,"and",b,"is",calc.mul())
    elif ch==4:
        print("Quotient of:",a,"and",b,"is",round(calc.div(),2))
    elif ch==5:
        print("Modulo of:",a,"and",b,"is",calc.mod())
    elif ch==6:
        break
    else:
        print("Invalid choice!!")
 
 
print()
