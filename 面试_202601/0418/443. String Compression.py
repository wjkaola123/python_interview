from collections import Counter, defaultdict, OrderedDict
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        k = 0
        od = OrderedDict()
        for c in chars:
            if c not in od:
                od[c] = 1
            else:
                od[c] += 1

        for key, val in od.items():
            if val == 1:
                chars[k] = key
                k += 1
            elif val >= 2 and val <= 9:
                chars[k] = key
                chars[k + 1] = f'{val}'
                k += 2
            else:
                # 10 or longer
                value_strings = str(val)
                n = len(value_strings)
                chars[k] = key
                k += 1
                for i in range(n):
                    chars[k] = value_strings[i]
                    k += 1

        return k


s = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
k = s.compress(chars)
assert k == 6
assert "".join(chars[:6]) == 'a2b2c3'

k = s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
assert k == 4
