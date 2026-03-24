class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ""
        return s.replace(" ", "%20")
