class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        left_str = s[0:n]
        return f'{s[n:]}{left_str}'


if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords("abcdefg", 2))
