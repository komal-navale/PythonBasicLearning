w = int(1.5)
x = float(2)
y = int('3')
z = str(6.1)
print(w)
print(x)
print(y)
print(z)
print('---------------------------------------------')

a = 3
b = 2
c = a*b
# If casting is not done here then "TypeError: must be str, not int" will be thrown at run time
print('a: '+str(a)+' & '+'b: '+str(b))
print('a multiply by b is '+str(c))