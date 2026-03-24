class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(' ')
        words = [item for item in words if item]
        # words.reverse()
        l = []
        for i in range(len(words) - 1, -1, -1):
            l.append(words[i])
        return ' '.join(l)

    def reverseWords2(self, s):
        """
        :param s:
        :return:
        """


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a good  example"))
