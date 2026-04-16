class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        p1 = p2 = 0

        while p1 < n and p2 < m:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        return True if p1 == n else False


s = Solution()
assert s.isSubsequence("axc", "ahbgdc") == False
