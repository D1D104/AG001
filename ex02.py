from sympy import Derivative, Integral, Symbol

matricula = 1988
c = matricula % 10
t = Symbol('T')


def v(t):
    return (5 * c) + (7 * t ** 4) + (pow(t, 1 / 3)) - (3 * c * t ** 3)


eqDeslocamento = Derivative(v(t), t).doit()
eqAceleracao = Integral(v(t), t).doit()

print("Equação do deslocamento ", eqDeslocamento)
print("Deslocamento para t =1: ", eqDeslocamento.subs({t: 1}))
print("Deslocamento para t =1: ", eqDeslocamento.subs({t: 7}))
print("Equação da acelerção ", eqAceleracao)
