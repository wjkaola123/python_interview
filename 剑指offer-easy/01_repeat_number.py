def find_repeat_number(nums):
    s = set()
    for val in nums:
        if val not in s:
            s.add(val)
        else:
            return val


if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5, 3, 1]
    print(find_repeat_number(numbers))
