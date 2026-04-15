from collections import Counter

# 异位词的考点
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # verify strings length
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # verify keys kinds
        if sorted(counter1.keys()) != sorted(counter2.keys()):
            return False

        # verify values frequency
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True
