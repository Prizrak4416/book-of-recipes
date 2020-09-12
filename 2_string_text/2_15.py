# Интерполяция переменных в строках


s = '{name} has {n} massages'
print(s.format(name='Yura', n=35))
name = "Vasia"
n = 10
print(s.format_map(vars()))