import collections


class Stack:

    def __init__(self):
        self._stack = collections.deque()

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self._stack) == 0


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        s = Stack()
        skip_pre_dict = collections.defaultdict(int)
        target = ""
        for part in paths:
            s.push(part)
        # 然后从栈中pop元素,并构造字符串
        while not s.is_empty():
            chars = s.pop()
            if chars in ['.', '']:
                continue
            elif chars == '..':
                skip_pre_dict["skip"] += 1
                continue
            else:
                if skip_pre_dict["skip"] == 0:
                    target = f'/{chars}' + target
                else:
                    skip_pre_dict["skip"] -= 1

        return target if target != "" else "/"


path = "/.../a/../b/c/../d/./"
s = Solution()
assert s.simplifyPath(path) == "/.../b/d"
assert s.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
