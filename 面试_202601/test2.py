import re

str1 = "Python's features"
str2 = re.match(r'(.*)on(.*) .*', str1, re.M | re.I)
print(str2.group(0))
print(str2.group(1))
print(str2.group(2))


class Example:
    def public_method(self):
        print("Public")

    def _protected_method(self):
        print("Protected by convention")

    def __private_method(self):
        print("Private with name mangling")


obj = Example()

# 访问情况
obj.public_method()  # ✅ 正常
obj._protected_method()  # ✅ 可以（但违反约定）
# obj.__private_method()      # ❌ AttributeError
obj._Example__private_method()  # ✅ 实际上可以（但千万别这样做）
