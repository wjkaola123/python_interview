from typing import List


class Solution:
    def is_contained_same_chars(self, word1: str, word2: str) -> bool:
        same_chars = [c for c in word1 if c in word2]
        return same_chars != []

    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if not self.is_contained_same_chars(words[i], words[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
