# Вычисления с комплексными числами
import cmath
import numpy as np

a = complex(2, 4)
print(a)
b = 3 - 5j
print(b)
print(a.real, a.imag)
print(a + b)
print(a * b)
print()

print(cmath.sin(a))
print(cmath.cos(a), '\n')

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))