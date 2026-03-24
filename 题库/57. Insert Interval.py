from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        if not intervals and newInterval:
            results.append(newInterval)
            return results

        is_merge = False
        is_add = False
        insert_index = -1
        for index, interval in enumerate(intervals):
            # 每个interval 拿出来和newInterval进行比较是否合并,is_merge 表示是否合并过, is_add表示是否插入到结果列表中
            if newInterval[0] > interval[1] or newInterval[1] < interval[0]:
                if is_merge and not is_add:
                    results.append([newInterval[0], newInterval[1]])
                    is_add = True
                results.append(interval)
                if not is_add:
                    if newInterval[1] < interval[0] and (
                            index - 1 >= 0 and newInterval[0] > intervals[index - 1][1] or index - 1 < 0):
                        insert_index = index
                    elif newInterval[0] > interval[1] and (index + 1 <= len(intervals) - 1 and newInterval[1] < \
                                                           intervals[index + 1][0] or index + 1 > len(intervals) - 1):
                        insert_index = index + 1
                    if insert_index != -1:
                        results.insert(insert_index, newInterval)
                        is_add = True
            else:
                is_merge = True
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not is_add:
            results.append(newInterval)

        return results

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        results = []
        i = 0
        intergvals_len = len(intervals)

        # 新区间左部分无重叠区间
        while i < intergvals_len and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1

        # 有重叠区间
        while i < intergvals_len and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        results.append([newInterval[0], newInterval[1]])

        # 新区间右部分无重叠区间
        while i < intergvals_len:
            results.append(intervals[i])
            i += 1

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.insert2([[1, 5]], [6, 8]))
