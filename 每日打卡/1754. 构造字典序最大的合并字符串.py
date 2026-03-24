class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        w1_len = len(word1)
        w2_len = len(word2)
        merge = []
        while p1 < w1_len and p2 < w2_len:
            if word1[p1:] >= word2[p2:]:
                merge.append(word1[p1])
                p1 += 1
            else:
                merge.append(word2[p2])
                p2 += 1

        if p1 < w1_len:
            merge.append(word1[p1:])
        if p2 < w2_len:
            merge.append(word2[p2:])

        return "".join(merge)


s = Solution()
print(s.largestMerge("cabaa", "bcaaa"))
