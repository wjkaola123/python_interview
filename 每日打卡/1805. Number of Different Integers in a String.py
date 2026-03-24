import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = re.findall('\d+', word)
        nums = [n.lstrip('0') for n in nums]
        return len(set(nums))

    def numDifferentIntegers2(self, word: str) -> int:
        return len(set(map(int, re.findall('\d+', word))))

    def numDifferentIntegers3(self, word: str) -> int:
        strs = re.sub('[a-z]+', ' ', word).strip()
        return 0 if not strs else len(set(map(int, strs.split(' '))))


if __name__ == '__main__':
    s = Solution()
    assert s.numDifferentIntegers3("a123bc34d8ef34") == 3
