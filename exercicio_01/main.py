from sympy import Limit, Symbol, oo

c = 331%10

def calculaLimite(x):
    return (1 + (c+4)/x**3)**(x**3)

x = Symbol('x')

resultado1 = Limit(calculaLimite(x), x, 0).doit()
resultado2 = Limit(calculaLimite(x), x, oo).doit()
resultado3 = Limit(calculaLimite(x), x, (-oo)).doit()

print(resultado1)
print(resultado2)
print(resultado3)



