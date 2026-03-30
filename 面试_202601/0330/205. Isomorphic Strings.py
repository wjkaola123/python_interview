class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = dict()
        start = 0
        end = len(s) - 1
        while start <= end:
            vals = d.values()
            if s[start] not in d:
                if t[start] not in vals:
                    d[s[start]] = t[start]
                else:
                    return False
            else:
                if d[s[start]] != t[start]:
                    return False
            start += 1

        return True


s = Solution()
assert s.isIsomorphic("egg", "add") == True
assert s.isIsomorphic("f11", "b23") == False
