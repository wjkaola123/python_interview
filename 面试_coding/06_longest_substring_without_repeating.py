class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        if len(arr) == 1:
            return 1

        max_count = 0
        for i in range(len(arr)):
            dic = {arr[i]: arr[i]}
            count = 1
            for c in arr[i+1:]:
                if c not in dic:
                    dic[c] = c
                    count += 1
                    max_count = max(max_count, count)
                else:
                    max_count = max(max_count, count)
                    break

        return max_count

s = "au"
print(Solution().lengthOfLongestSubstring(s))