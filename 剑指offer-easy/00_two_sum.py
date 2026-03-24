# This is a sample Python script.
import threading


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def towSum(nums, target):
    for index, num in enumerate(nums):
        other_num = target - num
        match = False
        if other_num in nums:
            for i, item in enumerate(nums):
                if item == other_num and i != index:
                    match = True
                    other_index = i
                    break
            if match:
                return index, other_index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(towSum(nums, target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
