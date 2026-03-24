from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        i, j, k, n = len(nums) - 2, len(nums) - 1, len(nums) - 1, len(nums) - 1

        # 第一步: 相邻的两个数比较， 找到 nums[i] < nums[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:  # 说明找到第一步满足条件的数据
            while k > 0:
                if nums[i] >= nums[k]:
                    k -= 1
                else:
                    break

            nums[i], nums[k] = nums[k], nums[i]  # 第二步: 找到倒序第一个比nums[i]大的数nums[k], 并交互两个数

        # 第三步：对j位置之后的所有降序排列的数做首尾交换
        while j < n:
            nums[j], nums[n] = nums[n], nums[j]
            j += 1
            n -= 1


if __name__ == '__main__':
    s = Solution()
    s.nextPermutation([1, 2, 3])
