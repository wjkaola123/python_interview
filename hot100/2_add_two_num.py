# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def get_sum(self, l):
        """
        根据列表得到数字
        :param l:
        :return:
        """
        num_list = []
        while l:
            num_list.append(l.val)
            l = l.next

        num_list = num_list[::-1]
        length = len(num_list)
        total_num = 0
        for i in range(length):
            weight = 10 ** i
            total_num += num_list[length - 1 - i] * weight

        return total_num

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total_num = self.get_sum(l1) + self.get_sum(l2)
        num_list = list(str(total_num))
        temp_list = []
        for i in range(len(num_list)):
            node = ListNode(int(num_list[i]))
            temp_list.append(node)
            if i > 0:
                temp_list[i].next = temp_list[i - 1]

        return temp_list[len(num_list) - 1]


if __name__ == '__main__':
    s = Solution()
    node13 = ListNode(9)
    node12 = ListNode(4, node13)
    l1 = ListNode(2, node12)

    node24 = ListNode(9)
    node23 = ListNode(4, node24)
    node22 = ListNode(6, node23)
    l2 = ListNode(5, node22)

    print(s.addTwoNumbers(l1, l2))
