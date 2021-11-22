#number and operators
x = 5
y = 2
print(x + y)
print(x * y)
print(x / y)
print(x % y)

#string and functions
x = 'hello'
y = 'world'
z = x + ', ' + y
print(z)
print(z.upper())
print(z.title())
print(len(z))
d = z.split(',')
print(d)
print(','.join(d))
print('{}\n{}'.format(x, y))

# conversion
x = 123
y = 345
print(str(x) + str(345))

# bool operators
a = 2
check = a == 2
print(check)
print(not check)

b = 3
check2 = b != 3
print(check2)
print(check and check2)
print(check or check2)

a = 'abcde'
print('d' in a)
print('d' not in a)
print(list(a))

# list
A = list(range(1, 5))
print(A)
print(A[1])
print(A[-1])

for x in A:
    print(x)

for i, x in enumerate(A):
    print(i, x)

# dictionary
A = {'a': 1, 'b': 2}
print(A['a'])

for k in A:
    print(k)
    
for k, v in A.items():
    print(k, v)

# user-defined function
def add_func(x, y=2):
    return x + y

print(add_func(1, 3))
print(add_func(1))

# numpy
import numpy as np
A = np.arange(6).reshape((2,3))

for row in A:
    for x in row:
        print(x, end=',')
    print()







