# Чистка строк


text = 'python\fis\tawesome\r\n'
print(text)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = text.translate(remap)
print(a)