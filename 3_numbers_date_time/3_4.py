# Работа с бинарными, восьмеричными и шестнадцатеричными целыми числами
x = 1234

print('bin', bin(x))
print('oct', oct(x))
print('hex', hex(x), '\n')

print('bin', bin(x)[2:], format(x, 'b'))
print('oct', oct(x)[2:], format(x, 'o'))
print('hex', hex(x)[2:], format(x, 'x'), '\n')

print(int('10011010010', 2))
print(int('2322', 8))
print(int('4d2', 16))