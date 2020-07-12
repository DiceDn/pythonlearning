from decorators import timer
#from decorators import *
from math import factorial

@timer
def add(a, b):
    '''adds inputs'''
    return a + b

print(add(1,2))

def mult(a, b):
    return a * b

print(mult(3,4))

#Functions are 1st class objects:
#list example and pythonic strategy design pattern:

#Can be assigned to other objects
add_new = add
print(add_new(5,6))

#ie. They can be used as arguments just like any other objects 
# (string, int, float, list etc).
list_1 = [add, mult]

print(list_1[0](5,5))

for f in list_1:
    print(f(3,4))

# how to decorate third party function:
# normal use of function:
fact_test = factorial(10)
print(f'factorial test result: {fact_test}')

# decorated function:
fact = timer(factorial)
fact_test = fact(10)
print(f'factorial test result: {fact_test}')
