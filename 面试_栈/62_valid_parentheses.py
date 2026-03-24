class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = list()
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False

                if stack and pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0


s = "]"
solution = Solution()
print(solution.isValid(s))

s1 = "()"
print(solution.isValid(s1))
