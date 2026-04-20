d = {"b": 5, "a": 10, "c": 2}

res = sorted(d.items(), key=lambda item: item[1])
d2 = {key: value for (key, value) in res}
print(d2)

d3 = dict(res)
print(d3)
