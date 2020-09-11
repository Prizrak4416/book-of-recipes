import re


text1 = '11/23/2020'
text2 = 'nov 12, 2020'
print(re.match(r'\d+/\d+/\d+', text1))
print(re.match(r'\d+/\d+/\d+', text2))

datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.match(text1))

text3 = "My besday in 12/24/2020 and naw 30/23/2020"
print(datepat.findall(text3))