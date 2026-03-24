import re


class Solution:
    def secondHighest(self, s: str) -> int:
        alist = re.findall("\d+", s)
        if not alist:
            return -1
        set_s = set()
        for item in alist:
            for letter in item:
                set_s.add(int(letter))
        sort_list = sorted(list(set_s))
        return sort_list[-2] if len(sort_list) > 1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.secondHighest('ck077'))
