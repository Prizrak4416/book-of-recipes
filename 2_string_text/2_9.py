# Нормализация текста в Unicode
import unicodedata


def out_red(text):
    return "\033[31m {}\033[0m" .format(text)
def out_green(text):
    return "\033[32m {}\033[0m" .format(text)

s1 = 'Spicy Jalape\u00f10'
s2 = 'Spicy Jalapen\u03030'

print(s1, s2)
print('s1=s2 -', out_red(s1 == s2))
print(len(s1), len(s2))

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print("\n", t1, t2)
print('t1=t2 -', out_green(t1 == t2))
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print("\n", t3, t4)
print('t3=t4 -', out_green(t3 == t4))
print(ascii(t3))