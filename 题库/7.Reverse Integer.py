class Solution:
    def reverse(self, x: int) -> int:

        max_num = pow(2, 31)

        if x < -max_num or x > max_num - 1:
            return 0

        is_less_than_zero = False
        if x < 0:
            is_less_than_zero = True
            x = abs(x)

        alist = list(str(x))
        alist.reverse()
        reverse_num = int(''.join(alist))
        if reverse_num < -max_num or reverse_num > max_num - 1:
            return 0

        return reverse_num if not is_less_than_zero else -reverse_num


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
