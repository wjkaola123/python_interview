import re

str1 = "Python's features"
str2 = re.match(r'(.*)on(.*) .*', str1, re.M | re.I)
print(str2.group(0))
print(str2.group(1))
print(str2.group(2))