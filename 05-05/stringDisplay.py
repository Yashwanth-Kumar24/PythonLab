class stringDisplay():
    s=''
    def accept(self):
        self.s=input("Enter string")
    def display(self):
        print(self.s)


dis=stringDisplay()
dis.accept()
dis.display()
