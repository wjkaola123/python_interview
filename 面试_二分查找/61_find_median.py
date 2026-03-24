from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merge_nums = sorted(nums1 + nums2, key=lambda x: x)
        length = len(merge_nums)
        if length % 2 == 0:
            return (merge_nums[length // 2 - 1] + merge_nums[length // 2]) / 2
        else:
            return merge_nums[length // 2]
