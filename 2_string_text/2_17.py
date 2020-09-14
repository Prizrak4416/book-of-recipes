# Работа с HTML и XPL сущностями в тексте
import html

text = '<div class="b-auth-social"> </div>'
print(text)
print(html.escape(text))
# отключить экранирование кавычек
print(html.escape(text, quote=False))