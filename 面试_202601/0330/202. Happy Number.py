class Solution:
    def isHappy(self, n: int) -> bool:
        d = dict()
        alist = list(str(n))
        ans = 0
        while ans != 1:
            keys = []
            ans = 0
            for e in alist:
                i = int(e)
                keys.append(f"{i}*{i}")
                ans = ans + i * i
            key = "+".join(keys)
            if key in d:
                return False  # 之前已经加过dict,则一定是无限循环
            else:
                d[key] = ans
            alist[:] = list(str(ans))
        return True


s = Solution()
assert s.isHappy(19) == True
assert s.isHappy(2) == False
