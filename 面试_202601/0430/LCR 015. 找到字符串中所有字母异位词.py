from typing import List, Counter


class Solution:

    def is_same_dict(self, d1: dict, d2: dict) -> bool:
        if len(d1) != len(d2):
            return False

        for key, val in d1.items():
            if key not in d2:
                return False

            if d2[key] != val:
                return False

        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        c1 = Counter(p)
        d1 = dict(c1.most_common())
        ans = []
        for i in range(n):
            c1 = Counter(s[i: i + m])
            d2 = dict(c1.most_common())
            if self.is_same_dict(d1, d2):
                ans.append(i)

        return ans


s = Solution()
assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
