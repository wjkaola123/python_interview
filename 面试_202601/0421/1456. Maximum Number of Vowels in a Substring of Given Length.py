from collections import deque


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        n = len(s)
        start = 0
        end = start + k - 1
        queue = deque()
        cnt = 0  # 统计元音
        while end < n:
            if start == 0:
                for i in range(start, end + 1):  # 第一次计算, start-end 范围统计
                    queue.append(s[i])
                    if s[i] in vowels:
                        cnt += 1
            else:
                c = queue.popleft()  # 队列左端pop出来一个头元素
                queue.append(s[end])  # 加入一个新元素
                if c in vowels:
                    cnt -= 1

                if s[end] in vowels:
                    cnt += 1

            ans = max(ans, cnt)
            start += 1
            end += 1

        return ans


s = Solution()
assert s.maxVowels("abciiidef", 3) == 3
