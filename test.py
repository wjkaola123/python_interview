def is_match(s):
    d = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    alist = list(s)
    for e in alist:
        if e in ("(", "[", "{"):
            stack.append(e)
        else:
            poped = stack.pop()
            if poped != d[e]:
                return False
    if not stack:
        return True
    else:
        return False


assert is_match("([]{})") == True
assert is_match("([)]") == False
assert is_match("(((") == False
