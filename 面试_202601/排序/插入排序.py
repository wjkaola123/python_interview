def insert_sort(nums):
    for i in range(1, len(nums)):
        current_value = nums[i]  # 从1的开始与之前的元素进行比较
        position = i

        while position > 0 and nums[position - 1] > current_value:  # 如果之前的元素都大于当前位置的元素
            nums[position] = nums[position - 1]  # 将元素依次向后移动一个位置
            position -= 1

        nums[position] = current_value  # 将当前元素插入到合适的位置

    return nums


"""
最好的情况是O(n)
最坏的情况是O(n**2)
"""
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print(alist)
