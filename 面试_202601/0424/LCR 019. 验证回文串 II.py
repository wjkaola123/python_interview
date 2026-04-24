class Solution:

    def is_palindrome(self, s: str, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                # 删除 start位置字符
                start += 1
                res1 = self.is_palindrome(s, start, end)
                # 删除 end位置字符
                start -= 1
                end = end - 1
                res2 = self.is_palindrome(s, start, end)

                return res1 or res2

        return True


s = Solution()
assert s.validPalindrome("abc") == False
