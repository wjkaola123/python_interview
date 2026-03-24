from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        results = []
        for index, interval in enumerate(intervals):
            if index == 0:
                results.append(interval)
            else:
                is_merged = False
                del_index = []
                temp = []
                for ind, item in enumerate(results):
                    if item[0] > interval[1] or item[1] < interval[0]:
                        pass
                    else:
                        min_val = item[0] if item[0] < interval[0] else interval[0]
                        max_val = item[1] if item[1] > interval[1] else interval[1]
                        if not temp:
                            temp = [min_val, max_val]
                        else:
                            temp[0] = min_val if min_val < temp[0] else temp[0]
                            temp[1] = max_val if max_val > temp[1] else temp[1]
                        del_index.append(ind)
                        is_merged = True
                if is_merged:
                    results.append(temp)
                else:
                    results.append(interval)

                del_index.reverse()
                for i in del_index:
                    del results[i]

        return results

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sort_intervals = sorted(intervals)
        results = []
        for index, interval in enumerate(sort_intervals):
            if index == 0:
                results.append(interval)
            else:
                last_interval = results[-1]
                if interval[0] > last_interval[1]:
                    results.append(interval)
                else:
                    last_interval[0] = min(interval[0], last_interval[0])
                    last_interval[1] = max(interval[1], last_interval[1])
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.merge2([[2, 3], [4, 6], [5, 7], [3, 4]]))
