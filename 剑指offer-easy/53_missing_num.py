class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if i != nums[i]:
                return i
        return nums[length - 1] + 1


if __name__ == '__main__':
    s = Solution()
    numbers = [0]
    print(s.missingNumber(numbers))
