from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        temp_list = []
        for item in nums:
            if item % 2 == 1:
                temp_list.insert(0, item)
            else:
                temp_list.append(item)

        return temp_list


if __name__ == '__main__':
    pass
