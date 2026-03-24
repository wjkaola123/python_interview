from collections import Counter
from typing import List


class Solution:

    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        point = 0
        point_two = 2

        while point_two < len(nums):

            if nums[point] == nums[point_two] and nums[point] == nums[point + 1]:
                nums.pop(point_two)
                point -= 1
                point_two -= 1

            point += 1
            point_two += 1
        return len(nums)


# def removeDuplicates(self, nums: List[int]) -> int:
#     c = Counter(nums)
#     del_index = []
#     pass_time_dict = {}
#     for index, n in enumerate(nums):
#         if c[n] > 2:
#             if n not in pass_time_dict:
#                 pass_time_dict.update({n: 1})
#             else:
#                 pass_time = pass_time_dict[n] + 1
#                 pass_time_dict.update({n: pass_time})
#                 if pass_time > 2:
#                     del_index.append(index)
#     del_index.reverse()
#     for index in del_index:
#         nums.pop(index)
#     return len(nums)


s = Solution()
assert s.removeDuplicates([1, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
