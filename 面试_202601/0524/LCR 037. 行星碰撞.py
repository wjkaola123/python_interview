from charset_normalizer.md import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
                continue

            while stack:
                if stack[-1] > 0:
                    if i > 0:
                        stack.append(i)
                        break
                    else:
                        # i < 0, 比较绝对值
                        if abs(stack[-1]) > abs(i):
                            break
                        elif abs(stack[-1]) == abs(i):
                            stack.pop()
                            break
                        else:
                            stack.pop()
                            if not stack:
                                stack.append(i)
                                break
                else:
                    stack.append(i)
                    break

        return stack


s = Solution()
print(s.asteroidCollision([5, 10, -5]))
print(s.asteroidCollision([8, -8]))
print(s.asteroidCollision([-2, -1, 1, 2]))
