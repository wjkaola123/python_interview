class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}

        length = len(nums) // 2

        for num in nums:
            c = nums.count(num)
            d.update({num: c})

        for key, val in d.items():
            if val > length:
                print(f"长度超过一半的数字:{key}")
                return key

    def majorityElement2(self, nums):
        """
        :param nums:
        :return:
        """
        d = {}
        length = len(nums) // 2
        for num in nums:
            if num not in d:
                d.update({num: 1})
            else:
                d.update({num: d.get(num) + 1})
            if d.get(num) > length:
                return num


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    # s.majorityElement(nums)
    print(s.majorityElement2(nums))
