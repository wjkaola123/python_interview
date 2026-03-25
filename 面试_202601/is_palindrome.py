class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = list(s)
        s = "".join([char for char in l if char.isalnum()])
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
