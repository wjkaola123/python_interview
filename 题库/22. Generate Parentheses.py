from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        result = []

        def dfs(parenthesis: str, left: int, right: int):
            if left == 0 and right == 0:
                results.append("".join(result))
                return

            if left == right:
                result.append("(")
                dfs("(", left - 1, right)
                result.pop()
            elif left < right:
                if left > 0:
                    result.append("(")
                    dfs('(', left - 1, right)
                    result.pop()
                result.append(")")
                dfs(')', left, right - 1)
                result.pop()

        dfs("", n, n)

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
