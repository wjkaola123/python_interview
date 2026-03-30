import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = collections.Counter(s)
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1

        for _, val in d.most_common():
            if val != 0:
                return False

        return True


s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
