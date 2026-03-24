import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = collections.OrderedDict()
        temp_list = list(s)
        for item in temp_list:
            if item not in d:
                d.update({item: 1})
            else:
                d.update({item: d.get(item) + 1})

        for key, val in d.items():
            if val == 1:
                return key

        return ' '


if __name__ == '__main__':
    pass
