def show(dic, **kwargs):
    print("inner dic:", id(dic))
    print("inner:", id(kwargs))
    print(kwargs)


kw = {"a": 1, "b": 2}
print("outer:", id(kw))
show(kw, **kw)


def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))

*a, _ = "RealPython"
print(a)
