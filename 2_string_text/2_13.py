# Выравнивание текстовых строк


text = 'Hello World'
print(text.ljust(20), '.')
print(text.rjust(20, '#'), '.')
print(text.center(20, '#'), '.', '\n')

print(format(text, '*>20'), '.')
print(format(text, '<20'), '.')
print(format(text, '#^20'), '.', '\n')

print('{:^10}{:#>10}'.format('hellow', 'world'), '\n')

x = 100.234567
print(format(x, '.2f'))