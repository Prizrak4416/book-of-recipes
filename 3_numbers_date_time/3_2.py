# Вычисление точных вычислений с десятичными дробями
from decimal import Decimal, localcontext


a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)