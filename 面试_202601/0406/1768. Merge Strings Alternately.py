class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = len(word1)
        m = len(word2)
        i = 1
        j = 0
        ans = [word1[0]]
        while i <= n - 1 and j <= m - 1:
            if j < i:
                ans.append(word2[j])
                j += 1
            else:
                ans.append(word1[i])
                i += 1

        while i <= n - 1:
            ans.append(word1[i])
            i += 1

        while j <= m - 1:
            ans.append(word2[j])
            j += 1

        return "".join(ans)


s = Solution()
assert s.mergeAlternately('abc', 'pqr') == 'apbqcr'
assert s.mergeAlternately('ab', 'pqrs') == 'apbqrs'
