from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in sorted_dict:
                sorted_dict[key] = []
            sorted_dict[key].append(s)

        return list(sorted_dict.values())
