class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # arr = sorted(arr)
        length = len(arr)
        for i in range(length):
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(arr)
        return arr[0:k]


if __name__ == '__main__':
    s = Solution()
    s.getLeastNumbers([1, 49, 3, 28, 5, 7], 3)
