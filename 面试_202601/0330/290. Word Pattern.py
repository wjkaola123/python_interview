class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        alist = s.split(' ')
        n = len(alist)
        d = {}
        if n != len(pattern):
            return False

        start = 0
        end = n - 1
        while start <= end:
            values = d.values()
            if alist[start] not in d:
                if pattern[start] in values:
                    return False
                else:
                    d[alist[start]] = pattern[start]
            else:
                if d[alist[start]] != pattern[start]:
                    return False
            start += 1

        return True
