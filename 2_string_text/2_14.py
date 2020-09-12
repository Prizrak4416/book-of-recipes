# Объединение и канкатенация строк


text = ['My', 'name', 'is', 'Yura']
print(' '.join(text))
print(','.join(text))

text = 'My name is'
name = 'Yura'
print('{} {}'.format(text, name))
print(text + ' ' + name)
print(text, name, sep=':')

def sample():
    yield 'My'
    yield 'name'
    yield 'is'
    yield 'Yura'

print(' '.join(sample()))

