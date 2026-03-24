class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        max_num = int(n * "9")
        return [item for item in range(1, max_num + 1)]


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(3))
