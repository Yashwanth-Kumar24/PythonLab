from packagedemo import sayHello,arithmetic
from packagedemo.subpackagedemo import printname

x=10
y=5
print(arithmetic.add(x,y))
print(arithmetic.subtract(x,y))

print(printname.printDetails('yashwanth','yash@gmail.com','98900'))

print(sayHello.sayHello('yash'))
