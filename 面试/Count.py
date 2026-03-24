from collections import Counter

c = Counter('gallahad')
print(c['a'])
print(c['l'])

c = Counter({'red': 4, 'blue': 2})
print(c['red'], c['blue'])

c = Counter(['eggs', 'ham', 'tom', 'eggs', 'aab'])
# del c['eggs']
print(c['eggs'], c['ham'], c['tom'], c['json'])
print(sorted(c.elements()))
