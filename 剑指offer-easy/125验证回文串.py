import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        compiler = re.compile(r"[a-zA-Z0-9]")
        temp_list = compiler.findall(s)
        temp_str = ''.join(temp_list).lower()
        start = 0
        end = len(temp_str) - 1

        while start < end:
            if temp_str[start] != temp_str[end]:
                return False
            start += 1
            end -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
