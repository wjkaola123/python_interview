class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [item for item in range(n)]
        del_index = -1
        while len(nums) > 1:
            for i in range(m):
                del_index += 1
                if del_index >= len(nums):
                    del_index = 0

            if del_index < len(nums):
                # 删除元素
                nums.pop(del_index)
                print(f"nums: {nums}")
                del_index -= 1
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(5, 3))
