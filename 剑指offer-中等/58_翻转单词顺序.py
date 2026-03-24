class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = [w for w in words if w]
        words_list = words[::-1]
        return " ".join(words_list)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a good   example"))
