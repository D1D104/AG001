#from sympy import Symbol, exp, solve
from sympy import *

c = 1988 % 10

def eq1(x):
    return exp(x-3)+exp(x-1)+exp(x)-(c+1)

def eq2(w):
    return (w ** 4) - (4 * w ** 3) + (3 * w) - c

def eq3(a):
    return (4*sin((c+1)*x)+2)

x = Symbol('x')
y = eq1(x)
result1 = solve(y)

w = Symbol('w')
z = eq2(w)
result2 = solve(z)

a = Symbol('a')
b = eq3(a)
result3 = solve(b)

print("Resultado da equação 1: ", result1)
print("Resultado da equação 2: ", result2)
print("Resultado da equação 3: ", result3)
