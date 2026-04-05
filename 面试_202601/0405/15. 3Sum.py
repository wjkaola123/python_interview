class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        s = set()
        for i in range(n):
            num1 = nums[i]
            for j in range(i + 1, n):
                num2 = nums[j]
                for k in range(j + 1, n):
                    num3 = nums[k]
                    if num1 + num2 + num3 == 0:
                        t = tuple(sorted([num1, num2, num3]))
                        s.add(t)

        ans = [[e[0], e[1], e[2]] for e in s]
        return ans


s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
