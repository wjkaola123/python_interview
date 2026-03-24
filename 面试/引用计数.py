import sys

# a = [1, 2]
#
# print(sys.getrefcount(a))

b = 1

print(sys.getrefcount(b))

import gc

print(gc.get_threshold())