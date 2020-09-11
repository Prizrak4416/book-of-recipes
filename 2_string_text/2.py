# Поиск текста в начале и в конце строки
from pathlib import Path


filname = 'vasia@mail.ru'
print(filname)
print('startswith', filname.startswith('vasia'))
print('endswith', filname.endswith(('.ru', '.tutu')))

files = Path('.').iterdir()
file = []
for p in files:
    if p.is_file():
        file.append(str(p))
print(file)

