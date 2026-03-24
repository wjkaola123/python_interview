nums_ = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    start = 0
    end = 1
    length = len(nums)
    while end < length:
        if nums[start] == nums[end]:
            nums.pop(end)
            length -= 1
        else:
            start = end
            end += 1

    return length


assert removeDuplicates(nums_) == 5
assert nums_ == [0, 1, 2, 3, 4]
