from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 1. 弹出popped 栈顶数字， 查询其在pushed栈中的位置, 该数字之前所有数字应该按倒序弹出， 否则返回false
        while popped:
            num = popped.pop(0)
            pushed_index = pushed.index(num)
            pre_pushed_nums = pushed[0:pushed_index]
            for n in popped:
                if n in pre_pushed_nums and n == pre_pushed_nums[-1]:
                    pre_pushed_nums.pop()
                elif n in pre_pushed_nums and n != pre_pushed_nums[-1]:
                    return False
            pushed.pop(pushed_index)

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
