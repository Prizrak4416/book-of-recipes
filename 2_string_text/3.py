# Поиск строк с использованием масок оболочки SHEL
from fnmatch import fnmatch, fnmatchcase


print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('Dat87.lb', 'Dat[0-9]*'))

adres = [
    '2345 n sdf sr',
    '233 n sdf sr',
    '234234n sdf sp',
    '23sdar n sdf sg',
]

mas = [a for a in adres if fnmatch(a, '* sr')]
print(mas)