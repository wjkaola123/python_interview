class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type:  head1: ListNode
        :rtype: ListNode
        """
        list_a = []
        while headA:
            list_a.append(headA)
            headA = headA.next

        while headB:
            if headB in list_a:
                return headB
            else:
                headB = headB.next

        return None


if __name__ == '__main__':
    pass
