class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        temp_list = []
        max_length = 0
        length = len(s)
        if length == 0 or length == 1:
            return length
        while j < length:
            if s[j] in temp_list:
                i = temp_list.index(s[j])
                temp_list = temp_list[i + 1:]
            temp_list.append(s[j])
            j += 1
            if len(temp_list) > max_length:
                max_length = len(temp_list)
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
