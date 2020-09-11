# поиск и замена текста без учета регистра
import re


text = 'USER Python, admin PYTHON, new_user python, end_user python'
print(re.findall('python', text, flags=re.IGNORECASE))
new_text = re.sub('python', 'c++', text, flags=re.IGNORECASE)
print(new_text)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('c++'), text, flags=re.IGNORECASE))