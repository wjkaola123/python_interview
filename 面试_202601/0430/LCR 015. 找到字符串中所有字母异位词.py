from typing import List


class Solution:

    def is_anagrams(self, s: str, p: str):
        if len(s) != len(p):
            return False

        if sorted(s) != sorted(p):
            return False

        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        ans = []
        for i in range(n):
            if self.is_anagrams(s[i: i + m], p):
                ans.append(i)

        return ans


s = Solution()
assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
