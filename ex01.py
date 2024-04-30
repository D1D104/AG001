from sympy import Limit, Symbol, S, Expr

matricula = 1988
c = matricula % 10
x = Symbol('X')

def function(x):
    return ((2 * x ** 2 - 7) / (7 * x ** 5 - 2)) * (c + 1)


resultado1: Expr = Limit(function(x), x, 1).doit()
resultado2: Expr = Limit(function(x), x, S.Infinity).doit()
resultado3: Expr = Limit(function(x), x, -S.Infinity).doit()

print('O limite para x-->1 é de', resultado1)
print('O limite para x-->+oo é de', resultado2)
print('O limite para x-->-oo é de', resultado3)
