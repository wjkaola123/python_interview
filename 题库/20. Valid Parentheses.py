class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        slength = len(s)
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        in_stack = ['(', '[', '{']
        stack = []
        point = 0

        while point < slength:

            if point == 0 and s[point] not in in_stack:
                return False

            if s[point] in in_stack:
                stack.append(s[point])
            else:
                if len(stack) == 0:
                    return False
                if d[s[point]] != stack[len(stack) - 1]:
                    return False
                stack.pop()
            point += 1

        if len(stack) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(){}}{"))
