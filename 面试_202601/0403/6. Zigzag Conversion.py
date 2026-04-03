class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c

            if i == 0 or i == numRows - 1:
                flag = -flag  # flag 非常巧妙的翻转列表行号
            i += flag

        return "".join(res)


s = Solution()
assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
