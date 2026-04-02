class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        alist = s.split(' ')
        return len(alist[-1])
