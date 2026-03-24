import re

# m = re.search('(?<=b)cdef', 'abcdef')

# print(m.group(0))
#
# print(re.split(r'\W+', 'Words, words, words.'))
#
# print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
#
# print(re.split(r'\b', 'Words, words, words.'))
#
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
#
# print(re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10'))
#
# pattern = re.compile("d")
#
# print(pattern.search("dog"))

m = re.findall(r"(\w+)\s(\w+)\W\s(\w+)", "Isaac Newton, physicist")
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
print(m)

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())

m = re.findall(r'\d+', '192ab22c56')
print(m)

m = re.findall(r'\d+', 'abc192aabbb87')
print(m)

s = re.split(r'\d+', 'A1B2C3D4')
print(s)

# matchlist = re.finditer(r'\d+', 'A1B2C3D4')
# print([item.group() for item in matchlist])
