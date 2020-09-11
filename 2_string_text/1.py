import re


line = 'asd jt. kta/, /ktjk,  !kdff, tjs a] kjfasd ;'
print(re.split(r'[;,.,!,/,\],\s]\s*', line))