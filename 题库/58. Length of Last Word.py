class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        alist = s.strip().split(" ")
        return len(alist[-1])
