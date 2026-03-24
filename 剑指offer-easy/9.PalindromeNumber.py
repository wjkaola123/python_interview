class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        temp = str(x)
        length = len(temp)
        start = 0
        end = length - 1
        while start < end:
            if temp[start] != temp[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(121) == True
