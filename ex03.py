from sympy import Integral, Symbol

c = 1988 % 10
x = Symbol('X')


def f(x):
    return (5*x**3) + ((5/(x/3))**(1/2))**3 + ((3/4)*x) - (3*c)


trabalho = Integral(f(x), (x, 3, 8)).doit()

print("O trabalho realizado entre as posições x = 3m e x = 8m é ", int(trabalho), "Joules")
