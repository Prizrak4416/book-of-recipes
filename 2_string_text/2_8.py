# Написание ругулярного выражения для многострочных шаблонов
import re


comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* tis is a 
multiline comment */'''

print(comment.findall(text1))

print(comment.findall(text2), '\n')

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text1))
print(comment.findall(text2), '\n')

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))