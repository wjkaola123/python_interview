class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []
        arr.extend(nums1)
        arr.extend(nums2)
        sort_arr = sorted(arr)
        length = len(sort_arr)
        middle_index = length // 2
        if length % 2 == 0:
            return (sort_arr[middle_index - 1] + sort_arr[middle_index]) / 2
        elif length % 2 == 1:
            return sort_arr[middle_index]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(s.findMedianSortedArrays(nums1, nums2))
    print(float((2 + 3) / 2))
