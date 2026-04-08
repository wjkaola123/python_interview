class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        alist = list(s)
        n = len(alist)
        start = 0
        end = n - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while start < end:
            if alist[start] not in vowels:
                start += 1

            if alist[end] not in vowels:
                end -= 1

            if alist[start] in vowels and alist[end] in vowels:
                alist[start], alist[end] = alist[end], alist[start]
                start += 1
                end -= 1

        return "".join(alist)


s = Solution()
assert s.reverseVowels("race a car") == "raca e car"
assert s.reverseVowels("Unglad, I tar a tidal gnu.") == "unglad, i tar a tIdal gnU."
