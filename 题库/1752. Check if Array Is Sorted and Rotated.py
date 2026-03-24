from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:

        point = 0
        point_next = 1
        length = len(nums)

        while point_next < length:
            if nums[point] <= nums[point_next]:
                point += 1
                point_next += 1
            else:
                break

        if point_next == length:  # 第一种情况: 数组是按升序排序
            return True

        # 第二种情况: 从point_next 位置开始以后的数字需按升序排列且都小于nums[0]
        while point_next < length:
            if point_next + 1 < length:  # 处理边界
                if nums[point_next] <= nums[point_next + 1]:
                    point_next += 1
                else:
                    break
            else:
                if nums[point_next] <= nums[0]:
                    point_next += 1
                else:
                    break

        if point_next == length and nums[0] >= nums[-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.check([1, 3, 2]))
