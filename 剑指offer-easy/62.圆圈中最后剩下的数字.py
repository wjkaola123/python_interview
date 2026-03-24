class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        li = [i for i in range(n)]

        del_index = -1
        while len(li) > 1:
            for i in range(m):
                del_index += 1
                if del_index > len(li) - 1:
                    del_index = 0

            li.pop(del_index)
            del_index -= 1

        return li[0]

    def lastRemaining2(self, n: int, m: int) -> int:
        li = [i for i in range(n)]

        del_index = n % m
        while len(li) > 1:
            pass

        return li[0]


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(5, 3))
