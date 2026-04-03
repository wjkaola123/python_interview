class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        alist = s.split(" ")
        alist = [chars for chars in alist if chars]
        alist.reverse()
        return " ".join(alist)


s = Solution()
assert s.reverseWords("the sky is blue") == "blue is sky the"
assert s.reverseWords("a good   example") == "example good a"
assert s.reverseWords("  hello world  ") == "world hello"
