# Разбивка текста на фиксированное количество колонок
import textwrap

text = "Fortune day out married parties. Latter remark hunted enough vulgar say man. As mr started arrival subject\
        by believe. Limits far yet turned highly repair parish talked six. Secure shy favour length all twenty denote.\
         He in sportsman household otherwise it perceived instantly. Whatever throwing we on resolved entrance together\
          graceful. Able rent long in do we. Any delicate you how kindness horrible outlived servants. In expression\
           an solicitude principles in do. Took sold add play may none him few. Made"

print(textwrap.fill(text, 50), '\n')
print(textwrap.fill(text, 70, initial_indent="   "), '\n')
print(textwrap.fill(text, 70, subsequent_indent='   '))