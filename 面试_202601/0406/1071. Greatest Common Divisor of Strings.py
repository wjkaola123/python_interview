class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        i = 0
        j = 0
        ans = []
        while i <= m - 1 and j <= n - 1:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            else:
                break

        # 计算长度
        if ans:
            strs = "".join(ans)
            num, rem = divmod(m, len(strs))
            if rem == 0:
                if strs * num == str1:
                    return strs
                else:
                    return ""
        else:
            pass

        return "".join(ans)
