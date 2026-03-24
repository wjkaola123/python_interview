from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [n for n in range(1, n + 1)]
        combinations = []
        combination = []

        def backtrack(nums: List[int]):
            if len(combination) == k:
                combinations.append(combination[:])
            else:
                for index, n in enumerate(nums):
                    combination.append(n)
                    backtrack(nums[index + 1:])  # 回溯 + 剪枝，访问前部分元素时一定会有和后部分的元素的组合，因此访问后部分元素时剪掉对前部分的元素的遍历,不会有重复的组合
                    combination.pop()

        backtrack(nums)
        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
