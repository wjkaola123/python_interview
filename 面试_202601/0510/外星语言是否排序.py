from itertools import pairwise
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        transformed = [[d[c] for c in word] for word in words]
        return all(s <= t for s, t in pairwise(transformed))


s = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert s.isAlienSorted(words, order) is True

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
assert s.isAlienSorted(words, order) is False
