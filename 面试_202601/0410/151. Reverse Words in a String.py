class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        alist = s.split(" ")
        alist = [word for word in alist if word != ""]
        alist.reverse()
        return " ".join(alist)
