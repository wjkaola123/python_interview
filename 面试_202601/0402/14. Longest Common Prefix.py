from collections import defaultdict
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = []
        # 利用 zip
        for chars in zip(*strs):
            if len(set(chars)) == 1:  # 所有字符串当前位置字符相同
                result.append(chars[0])
            else:
                break

        return ''.join(result)


s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix


s = Solution2()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
