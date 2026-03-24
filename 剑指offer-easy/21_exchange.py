class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = []
        l2 = []
        for n in nums:
            if n % 2 == 1:
                l1.append(n)
            else:
                l2.append(n)
        for item in l2:
            l1.append(item)
        return l1


if __name__ == '__main__':
    s = Solution()
    print(s.exchange([1, 2, 3, 4]))
