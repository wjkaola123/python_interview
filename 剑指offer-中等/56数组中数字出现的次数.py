from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        d = {}
        for n in nums:
            if n not in d:
                d.update({n: 1})
            else:
                d.update({n: d[n] + 1})
        res = []
        for key, value in d.items():
            if value == 1:
                res.append(key)
        return res


class Solution1:
    # 异或（ ^ ）是一个数学运算符。它应用于逻辑运算。异或的数学符号为“⊕”，计算机符号为“ ^ ”。
    # 二进制下异或运算法则：
    # 1 ^ 1 = 0
    # 0 ^ 0 = 0
    # 1 ^ 0 = 1
    # 0 ^ 1 = 1
    # 因此十进制下相同数字异或结果为0，数字a与0异或结果仍为原来的数字a。

    def singleNumbers2(self, nums: List[int]) -> List[int]:
        x = 0
        for n in nums:
            x ^= n
        return x

    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        a, b = 0, 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0
        h = 1
        while ret & h == 0:
            h <<= 1
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n

        return [a, b]


if __name__ == '__main__':
    s = Solution1()
    # print(s.singleNumbers([1, 2, 1, 2, 3, 3, 5, 7, 9, 7, 9]))
    print(5 ^ 7 ^ 7 ^ 9 ^ 9)
