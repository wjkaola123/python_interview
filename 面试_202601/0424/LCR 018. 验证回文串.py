class Solution:
    def isPalindrome(self, s: str) -> bool:
        alist = list(s)
        alist = [c.lower() for c in alist if c.isdigit() or c.isalpha()]
        start = 0
        end = len(alist) - 1

        while start < end:
            if alist[start] == alist[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
