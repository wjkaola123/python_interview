from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def get_permu(s: str, cur_s: str, result=List[str]):
            if not s:
                result.append(cur_s)
                return
            if len(result) < k:
                for i in range(len(s)):
                    get_permu(s[:i] + s[i + 1:], cur_s + s[i], result)

        s = ''
        for i in range(1, n + 1):
            s += str(i)
        result = []
        get_permu(s, '', result)
        return result[- 1]


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 9))
