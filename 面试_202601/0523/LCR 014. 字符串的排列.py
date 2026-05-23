from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1)
        c1 = Counter(s1)
        list1 = sorted(c1.most_common())
        l2 = len(s2)
        for i in range(l2 - l1 + 1):
            c2 = Counter(s2[i: i + l1])
            list2 = sorted(c2.most_common())
            if list1 == list2:
                return True

        return False


s = Solution()
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("adc", "dcda") == True
