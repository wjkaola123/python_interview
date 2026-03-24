from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 插入排序
        num1_len = m
        for n2 in nums2:
            current_val = n2
            position = num1_len - 1
            while position >= 0 and current_val < nums1[position]:
                nums1[position + 1] = nums1[position]
                position -= 1

            nums1[position + 1] = current_val
            num1_len += 1


s = Solution()
nums1 = [2, 0]
nums2 = [1]
s.merge(nums1, 1, nums2, 1)
print(nums1)
