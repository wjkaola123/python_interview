class Solution:
    def minOperations(self, s: str) -> int:

        c1 = 0
        c2 = 0
        alist = list(s)
        alist2 = list(s)

        # 第一个字符不变的计算
        for i in range(1, len(alist)):
            if alist[i] == alist[i - 1]:
                alist[i] = "1" if alist[i - 1] == "0" else "0"
                c1 += 1

        # 第一个字符变化的计算
        alist2[0] = "1" if alist2[0] == "0" else "0"
        for i in range(1, len(alist2)):
            if alist2[i] == alist2[i - 1]:
                alist2[i] = "1" if alist2[i - 1] == "0" else "0"
                c2 += 1

        return min(c1, c2 + 1)


if __name__ == '__main__':
    # s = Solution()
    # print(s.minOperations("1111"))

    s = "111010"
    # 如果第一个字符为0
    print(s[0::2].count('1') + s[1::2].count('0'))

    # 如果第一个字符为1
    print(s[0::2].count('0') + s[1::2].count('1'))
