from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        alist = []
        n1 = nums1[:m]
        n2 = nums2[:n]
        while n1 and n2:
            if n1[0] < n2[0]:
                alist.append(n1.pop(0))
            else:
                alist.append(n2.pop(0))

        alist.extend(n1 if n1 else n2)
        nums1[:] = alist


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

sol = Solution()
sol.merge(nums1, 3, nums2, 3)
print(nums1)


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
