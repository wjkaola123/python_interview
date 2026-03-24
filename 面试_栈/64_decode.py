class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur

                stack.pop()  # 弹出 '['
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(cur * int(num))
            else:
                stack.append(char)

        return "".join(stack)
