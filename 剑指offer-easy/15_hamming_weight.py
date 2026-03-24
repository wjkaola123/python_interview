class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

    def hammingWeight2(self, n):
        """
        :param n:
        :return:
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(11))
    print(s.hammingWeight2(11))
