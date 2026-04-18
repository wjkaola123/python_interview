from collections import Counter, defaultdict, OrderedDict
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        n = len(chars)
        start = end = 0
        k = 0
        while end < n:
            while end < n and chars[start] == chars[end]:
                end += 1

            length = end - start
            if length == 1:
                chars[k] = chars[start]
                k += 1
            elif length >= 2 and length <= 9:
                chars[k] = chars[start]
                chars[k + 1] = f'{length}'
                k += 2
            else:
                # 10 or longer
                value_strings = str(length)
                num_length = len(value_strings)
                chars[k] = chars[start]
                k += 1
                for i in range(num_length):
                    chars[k] = value_strings[i]
                    k += 1
            start = end
        return k


s = Solution()
# test case 1
chars = ["a", "a", "b", "b", "c", "c", "c"]
k = s.compress(chars)
assert k == 6
assert "".join(chars[:6]) == 'a2b2c3'

# test case 2
k = s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
assert k == 4

# test case 3
chars = ["a", "b", "c"]
s.compress(chars)
print(chars)

# test case 4
chars = ["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
         "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]
s.compress(chars)
print(chars)
