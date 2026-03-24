from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

m = ChainMap(adjustments, baseline)
print(dir(m))
print(m.maps)

for key, value in m.items():
    print(f'{key}:{value}')
