from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_array = sorted(list(p))
        p_len = len(p_array)
        indexes = []
        for index in range(s_len):
            if sorted(list(s[index: index + p_len])) == p_array:
                indexes.append(index)

        return indexes


s = Solution()
print(s.findAnagrams('cbaebabacd', 'abc'))