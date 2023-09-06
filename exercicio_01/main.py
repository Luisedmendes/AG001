from sympy import Limit, Symbol, oo

c = 331%10

def calculaLimite(x):
    return (1 + (c+4)/x**3)**(x**3)

x = Symbol('x')

resultado1 = Limit(calculaLimite(x), x, 0).doit()
resultado2 = Limit(calculaLimite(x), x, oo).doit()
resultado3 = Limit(calculaLimite(x), x, (-oo)).doit()

print("Limite com x tendendo a 0 = ",resultado1)
print("Limite com x tendendo a mais oo = ",resultado2)
print("Limite com x tendendo a menos oo = ", resultado3)



