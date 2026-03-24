from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = len(words)
        max_multi = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                common_set = set(words[i]).intersection(set(words[j]))
                if common_set:
                    continue
                else:
                    multi = len(words[i]) * len(words[j])
                    max_multi = multi if multi > max_multi else max_multi

        return max_multi


if __name__ == '__main__':
    s = Solution()
    assert s.maxProduct(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]) == 16
