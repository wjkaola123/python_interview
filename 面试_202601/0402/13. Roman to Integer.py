class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        start = 0
        end = start + 1
        n = len(s)
        ans = 0
        while end < n:
            if s[start] == 'I' and s[end] in ['V', 'X']:
                if s[end] == 'V':
                    ans += 4
                elif s[end] == 'X':
                    ans += 9
                start += 2
                end += 2
            elif s[start] == 'X' and s[end] in ['L', 'C']:
                if s[end] == 'L':
                    ans += 40
                elif s[end] == 'C':
                    ans += 90
                start += 2
                end += 2
            elif s[start] == 'C' and s[end] in ['D', 'M']:
                if s[end] == 'D':
                    ans += 400
                elif s[end] == 'M':
                    ans += 900
                start += 2
                end += 2
            else:
                ans += d[s[start]]
                start += 1
                end += 1

        if start == n - 1:
            ans += d[s[start]]

        return ans


s = Solution()
assert s.romanToInt('III') == 3
assert s.romanToInt('LVIII') == 58
assert s.romanToInt('MCMXCIV') == 1994


class Solution2:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        ans = 0
        n = len(s)

        for i in range(n):
            # 如果当前字符小于下一个字符，说明是减法组合
            if i < n - 1 and d[s[i]] < d[s[i + 1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]

        return ans
