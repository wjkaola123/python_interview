class Solution:

    def is_palindrome(self, s: str, i: int, j: int):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        if n < 2:
            return 1

        for i in range(n):
            for j in range(i, n):
                if self.is_palindrome(s, i, j):
                    cnt += 1

        return cnt
