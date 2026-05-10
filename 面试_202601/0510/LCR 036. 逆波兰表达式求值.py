from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if not stack:
                stack.append(int(t))
                continue

            if t in ['+', '-', '*', '/']:
                n2 = stack.pop()
                n1 = stack.pop()
                match t:
                    case '+':
                        res = n1 + n2
                    case '-':
                        res = n1 - n2
                    case '*':
                        res = n1 * n2
                    case '/':
                        res = int(n1 / n2)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]


s = Solution()
assert (s.evalRPN(["4", "13", "5", "/", "+"])) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
