# Срезание нежелательных символов из строк
import re

text = "  Hellow world \n "
print(text.strip())
print(text.lstrip())
print(text.rstrip(), "\n")

text2 = "-- new text and __"
print(text2.strip('-'))
print(text2.strip('_'))
print(text2.strip('_-'), "\n")

text3 = " Tis is new         text       and __"
print(text3)
print(text3.replace(' ', ''))
print(re.sub('\s+', ' ', text3))
