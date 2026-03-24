class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, target)]
        results = []
        for i in range(target):
            s = 0
            num_list = []
            for j in range(i, len(nums)):
                if s < target:
                    num_list.append(nums[j])
                    s += nums[j]
                elif s == target:
                    results.append(num_list)
                    break
                elif s > target:
                    break

        return results

    def findContinuousSequence2(self, target):
        """
        :param target:
        :return:
        """
        res = []
        l = 1
        r = 2
        while l < r:
            a = []
            sum = (l + r) * (r - l + 1) / 2
            if sum < target:
                r += 1
            elif sum > target:
                l += 1
            else:
                for i in range(l, r + 1):
                    a.append(i)
                res.append(a)
                l += 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.findContinuousSequence(9)
