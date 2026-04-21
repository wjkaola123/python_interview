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
                for i in range(start, end + 1):
                    queue.append(s[i])
                    if s[i] in vowels:
                        cnt += 1
            else:
                c = queue.popleft()
                queue.append(s[end])
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
