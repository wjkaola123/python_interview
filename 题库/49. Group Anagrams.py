from collections import Counter, OrderedDict
from typing import List


class Solution:
    # 正确思路，利用哈希表，对每个字符串排序分类解法
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sort_str = "".join(sorted(s))
            if sort_str not in d:
                d.update({sort_str: [s]})
            else:
                d[sort_str].append(s)
        return [val for val in d.values()]

    def get_key(self, s: str):
        c = Counter(s)
        key = ''
        for letter in sorted(c):
            key += f"{letter}{c.get(letter)}"

        return key

    # 利用{字母+个数...} 作为key值进行归类
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = self.get_key(s)
            if key not in d:
                d.update({key: [s]})
            else:
                d[key].append(s)

        return [val for val in d.values()]


if __name__ == '__main__':
    s = Solution()
    # print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
