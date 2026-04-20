class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        chars = []
        digits = []

        for i in range(n):
            if s[i].isdigit() or s[i].isalpha() or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                chars.reverse()
                # pop 出 "["
                stack.pop()
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                digits.reverse()
                string = "".join(chars)
                num = int("".join(digits))
                decode_string = num * string
                stack.extend(list(decode_string))
                chars = []
                digits = []

        return "".join(stack)


s = Solution()
res = s.decodeString("3[a]2[bc]")
assert res == "aaabcbc"
res = s.decodeString("3[a2[c]]")
assert res == "accaccacc"
