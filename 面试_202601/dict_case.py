a = {"a": "A", "b": None}
b = {"a": None, "b": "B"}

a.update({k: v for k, v in b.items() if v is not None})
print(a)
