from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     target_index = length - 1
    #     paths = []
    #     path = []
    #
    #     def dfs(current_index, steps: List[int]):
    #         if not steps and current_index != target_index:
    #             return
    #         for step in steps:
    #             if current_index + step == target_index:
    #                 path.append(step)
    #                 paths.append(path[:])
    #                 path.pop()
    #             elif current_index + step < target_index:
    #                 path.append(step)
    #                 next_steps = list(
    #                     range(1, nums[current_index + step] + 1) if nums[current_index + step] >= 1 else range(0))
    #                 dfs(current_index + step, next_steps)
    #                 path.pop()
    #
    #     first_steps = list(range(1, nums[0] + 1) if nums[0] >= 1 else range(0))
    #     dfs(0, first_steps)
    #     print(paths)
    #     print([path for path in paths if len(path) == 5])
    #     return min([len(path) for path in paths]) if paths else 0

    def jump(self, nums: List[int]) -> int:

        ## 整体思路是通过遍历当前区域维护变量max_pos，计算从当前区域(的某一点)通过一跳可跃至的最远距离
        ## 当遍历到当前区域的最末端时，维护完毕，可以开始展望下一跳的落点。我们无需计算下一跳的精确落点，只要知道落点的范围即可：下一跳必需落在
        ## [end+1, max_pos]区间里，此时我们令step加一，表示步入下一个区域，同时更新end为下一个区域的末端：end = max_pos

        ## 初始时处于第一片区域[0,0]，只包含一个点pos = 0， 所以当我们遍历该区域时，遍历到的第一个点也是该区域的终点：
        ## 遍历第一个点pos=0时，首先维护 max_pos = pos + nums[pos] = nums[0]，接着判断出已遍历完当前区域(pos == end)，因而更新step，end

        ## 当走到倒数第二个位置(pos = n-2)时，由end定义显然有end >=pos = n-2, 若end = pos = n-2，说明终点(n-1)位于下一个区域，还需一跳才能抵达
        ## 若 end >pos = n-2，即end >= n-1，说明当前区域包括终点，无需额外的一跳来抵达终点，step无需加一

        ans = 0
        start = 0
        end = 0
        while end < len(nums) - 1:
            maxPos = 0
            for i in range(start, end + 1):
                maxPos = max(maxPos, i + nums[i])  # 能跳到最远的距离

            start = end + 1  # 下一次起跳点范围开始的格子
            end = maxPos  # 下一次起跳点范围结束的格子
            ans += 1  # 跳跃次数

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))

    # print(list(range(1, 3)))
