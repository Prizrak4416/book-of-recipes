# Формирование числа для вывода
x = 1234.56789

print(format(x, '0.2f'), '::', '{:.2f}'.format(x))
print(format(x, '^20.2f'))
print(format(x, '0,.2f'), '::', '{:0,.2f}'.format(x))