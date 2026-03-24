from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                backtrack(j + 1, tmp + [nums[j]])

        backtrack(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3, 4]))
