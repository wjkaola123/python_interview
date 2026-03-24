import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ' '
        d = collections.OrderedDict()
        for c in s:
            if c not in d:
                d.update({c: 1})
            else:
                d.update({c: d.get(c) + 1})

        for key, val in d.items():
            if val == 1:
                return key
        return ' '


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("cc"))
