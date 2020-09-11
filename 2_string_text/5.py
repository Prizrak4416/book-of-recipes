# Поиск и замена текста
import re

text = 'my name is vasia, vasia the best name, vasia'

new_text = text.replace('vasia', 'yura')
print(text)
print(new_text, '\n')

text = 'my name is 27/12/2020, 13/12/2020 the best name, 01/12/1012'
new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2-\1-\3', text)
print(text)
print(new_text)