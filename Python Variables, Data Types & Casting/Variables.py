# 1. A variable is created the moment you first assign a value to it.
x = 5
y = "User"
print(x)
print(y)

# 2. Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 10
a = "Admin"
print(a)    # This will show last assigned value to same variable. In this case it is Admin

# 3. You can get the data type of a variable with the type() function.
z = 12
print(type(z))

# 4. String variables can be declared either by using single or double quotes.
b = "John"
# is the same as
b = 'John'

# 5. Variable names are case-sensitive.
c = 4
C = "Hello"
# C will not overwrite c

# Variable Names
# Legal variable names
myvar = "Komal"
my_var = "Komal"
_my_var = "Komal"
myVar = "Komal"
MYVAR = "Komal"
myvar2 = "Komal"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Illegal variable name:
2myvar = "Komal"
my-var = "Komal"
my var = "Komal"

#This example will produce an error in the result

# 1. Assigning many values to multiple variables
x, y, z = "Mango", "Banana", "Chikoo"
print(x)
print(y)
print(z)

# 2. Assigning one value to multiple variables
a = b = c = 5
print(a)
print(b)
print(c)

# 3. Unpack a collection
vehicles = {"Car", "Bicycle", "Truck"}
p, q, r = vehicles
print(p)
print(q)
print(r)

#Output Variables
x = "Object Oriented"
print("Python is "+x)

a = 2
b = 5
c = a+b
print('Value of c is '+str(c))

p = 9
q = 5
print(p-q)

y = "Add"
z = 5
print(y+z)


# Global Variables
x = "Server side web development"
def myFunc1():
    x = "Machine Learning"
    print('Python is used in '+x)

myFunc1()
print('Python is used in '+x)

print('------------------------------------------------')
#Global keyword
x = "awesome"
def myFunc2():
    global x
    x = "popular"

myFunc2()
print('Python is '+x)









