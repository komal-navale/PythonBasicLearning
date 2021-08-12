# A] Strings
# Assign String to a Variable
print('-----------------------------------------------------------------------------------')
x = "Hello World!"
print(x)
print('-----------------------------------------------------------------------------------')

# Multiline Strings
a = """It is possible to write Python in an Integrated Development Environment, 
such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful 
when managing larger collections of Python files."""
print(a)

"""a = '''It is possible to write Python in an Integrated Development Environment, 
such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful 
when managing larger collections of Python files.'''
print(a)"""
print('-----------------------------------------------------------------------------------')

# Strings are Arrays
print(x[1])
print('-----------------------------------------------------------------------------------')

# Looping Through a String
y = "PYTHON"
for c in y:
    print(c)
print('-----------------------------------------------------------------------------------')

# String Length
print(len(y))
print('-----------------------------------------------------------------------------------')

# Check String
txt = "The best things in life are free!"
print("things" in txt)

if "things" in txt:
    print("Yes, 'things' is present")
print('-----------------------------------------------------------------------------------')

# Check if NOT
print("exclusive" in txt)

if "exclusive" not in txt:
    print("No, 'exclusive' is not present")
print('-----------------------------------------------------------------------------------')


print('-----------------------------------------------------------------------------------')
# B] String Slicing
x = "Python is very Popular"
print(x)
print('-----------------------------------------------------------------------------------')
# Slicing
print(x[0:6])
print('-----------------------------------------------------------------------------------')
# Slice From the Start
print(x[0:])
print('-----------------------------------------------------------------------------------')
# Slice To the Start
print(x[:6])
print('-----------------------------------------------------------------------------------')
# Negative Indexing
print(x[-5:-2])
'''From: "p" in "Popular" (position -5)
To, but not included: "a" in "Popular" (position -2) so pul '''
print('-----------------------------------------------------------------------------------')


# C] Python - Modify Strings
x = "Hello, World!"
print(x)
print('-----------------------------------------------------------------------------------')
# Upper Case
print(x.upper())
print('-----------------------------------------------------------------------------------')
# Lower Case
print(x.lower())
print('-----------------------------------------------------------------------------------')
# Remove Whitespace
print(x.strip())
print('-----------------------------------------------------------------------------------')
# Replace string
print(x.replace("H", "Y"))
print('-----------------------------------------------------------------------------------')
# Split string
print(x.split(","))
print('-------------------------------------------------------------')

# D] String Concatenation
a = "Hello"
b = "Python!"
print(a+b)
print('---------------------------------')
# Add space
print(a+" "+b)
print('-------------------------------------------------------------')
# E] Python - Format - Strings
age = 27
txt = "My name is Komal and I am {} years old"
print(txt.format(age))
print('-------------------------------------------------------------')

quantity = 10
itemNo = 1234
price = 100     # float(100) also can be assigned to price
txt = "I want {} pieces of item {} for {} rupees."
print(txt.format(quantity, itemNo, price))

print('-------------------------------------------------------------')
quantity = 5
itemNo = 2345
price = 49.95
txt = "I want to pay {2} rupees for {0} pieces of item {1}."
print(txt.format(quantity, itemNo, price))
print('-------------------------------------------------------------')
# F] Escape Character

txt = "We are the \"Maratha's\" from the west part of India."

print(txt)
print('-------------------------------------------------------------')
# G] Python - String Methods
x = "python is very Popular"
y = "2.5"
print(x.capitalize())
print(x.center(5))
print(x.casefold())
print(x.count('Popular'))
print(x.encode())
print(x.endswith('r'))
print(x.find('very'))
print(x.isalnum())





