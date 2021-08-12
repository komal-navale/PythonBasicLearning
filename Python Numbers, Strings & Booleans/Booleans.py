print(10 > 9)
print(10 == 9)
print(10 < 9)
print('-------------------------------------')
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print('-------------------------------------')
print(bool("Hello"))
print(bool(15))
print('-------------------------------------')
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print('-------------------------------------')
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print('-------------------------------------')
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('-------------------------------------')
class myClass:
    def __len__(self):
        return 0
myObj = myClass()
print(bool(myObj))

print('-------------------------------------')

def myFunc():
    return True

if myFunc():
    print('Yes! true')
else:
    print('No! False')

print('-------------------------------------')




