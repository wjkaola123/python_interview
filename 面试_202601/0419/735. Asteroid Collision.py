from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            else:
                stop_compare = False  # 是否停止比较栈顶元素与当前元素
                while not stop_compare:
                    # 比较当前元素和栈顶元素
                    if stack[-1] * ast > 0:  # 符号相同
                        stack.append(ast)
                        stop_compare = True
                    else:
                        # 栈顶元素符号和当前元素不同, 分成两种情况:
                        # 1. 栈顶为负数,当前数为正,则不会相撞
                        # 2. 栈顶为正数,当前数为负,则会相撞
                        if stack[-1] < 0 and ast > 0:
                            stack.append(ast)
                            stop_compare = True
                        elif stack[-1] > 0 and ast < 0:
                            if abs(stack[-1]) > abs(ast):  # 栈顶元素质量 > 当前元素质量
                                stop_compare = True
                            elif abs(stack[-1]) == abs(ast):  # 栈顶元素质量 == 当前元素质量
                                stack.pop()
                                stop_compare = True
                            elif abs(stack[-1]) < abs(ast):  # 栈顶元素质量 < 当前元素质量
                                stack.pop()
                                stop_compare = False
                                if not stack:
                                    stack.append(ast)  # 栈为空时, 加入当前元素
                                    stop_compare = True

        return stack


asteroids = [3, 5, -6, 2, -1, 4]
s = Solution()
assert s.asteroidCollision(asteroids) == [-6, 2, 4]
