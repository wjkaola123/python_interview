from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)

        return list(d.values())


s = Solution()
assert s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
