"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for c in ransomNote:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False

        return True

s = Solution()
assert s.canConstruct("a", "b") == False
assert s.canConstruct("aa", "aab") == True
