class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        chars = []
        digits = []

        for i in range(n):
            if s[i].isdigit() or s[i].isalpha() or s[i] == '[':  # 数字,字母,[ 直接加入栈中
                stack.append(s[i])
            elif s[i] == ']':
                while stack and stack[-1] != '[':  # 弹出"["后面所有的字母
                    chars.append(stack.pop())
                chars.reverse()  # 翻转
                stack.pop()  # pop 出 "["
                while stack and stack[-1].isdigit():  # 弹出"["前面的所有数字
                    digits.append(stack.pop())
                digits.reverse()  # 翻转
                string = "".join(chars)
                num = int("".join(digits))
                decode_string = num * string  # 解码弹出的数字和字母
                stack.extend(list(decode_string))  # 再次压入栈中
                chars = []  # 清空,以便下一轮解析
                digits = []  # 清空,以便下一轮解析

        return "".join(stack)  # ""连接返回栈中的所有字母


s = Solution()
res = s.decodeString("3[a]2[bc]")
assert res == "aaabcbc"
res = s.decodeString("3[a2[c]]")
assert res == "accaccacc"
