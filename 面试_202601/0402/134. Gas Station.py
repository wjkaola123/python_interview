from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                ind = (i + cnt) % n  # 环形索引
                sum_of_gas += gas[ind]
                sum_of_cost += cost[ind]
                if sum_of_gas < sum_of_cost:
                    break  # 说明从i出发无法闭环

                cnt += 1
            # 如果能完整走 n 站，说明起点 i 可行
            if cnt == n:
                return i
            else:
                """
                设从 i 到 k（i ≤ k ≤ i+cnt）之间的累计油量差（gas - cost）总是非负（否则早就停了），
                但既然从 i 到 i+cnt+1 就失败，意味着从 i 出发累积到 i+cnt+1 时总油量 < 总油耗。
                若从中间某个 k 出发，相当于去掉前一段 i→k 的油量（这部分非负），
                到达 i+cnt+1 时的总油量只会更少，所以更不可能成功。
                因此可以直接跳过
                """
                i += cnt + 1

        return -1


s = Solution()
assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
