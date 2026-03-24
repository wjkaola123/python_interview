class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 考虑双指针做法
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        if t_len == 0:
            return False

        s_point = t_point = 0

        while t_point < t_len:

            if t[t_point] == s[s_point]:
                s_point += 1

            if s_point > s_len - 1:
                return True

            t_point += 1

        return False

    def isSubsequence(self, s: str, t: str) -> bool:
        # 用队列实现
        s_len = len(s)
        t_len = len(t)
        if s_len == 0:
            return True
        if t_len == 0:
            return False
        queue = [item for item in s]
        t_point = 0
        while t_point < t_len:
            if t[t_point] == queue[0]:
                queue.pop(0)

            if len(queue) == 0:
                return True
            t_point += 1

        return False


if __name__ == '__main__':
    s = Solution()
    # assert s.isSubsequence("b", "abc") is True
    assert s.isSubsequence("abc", "ahbgdc") is True
    # assert s.isSubsequence("axc", "ahbgdc") is False
