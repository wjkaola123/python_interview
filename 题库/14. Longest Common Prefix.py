from typing import List


class Solution:

    @classmethod
    def get_common_prefix(cls, str1: str, str2: str) -> str:
        i = 0
        length1 = len(str1)
        length2 = len(str2)
        while i < length1 and i < length2:
            if str1[i] != str2[i]:
                break
            i += 1
        return str1[0:i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        if not strs:
            return common_prefix
        for index, item in enumerate(strs):
            if index == 0:
                common_prefix = item
            else:
                common_prefix = self.get_common_prefix(common_prefix, item)

        return common_prefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
