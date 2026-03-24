class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for item in s:
            if item not in d:
                d.update({item: 1})
            else:
                return item
        return ""
