# Определение регулярных выражений для поиска кратчайшего совпадения
import re


str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Coumputer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
