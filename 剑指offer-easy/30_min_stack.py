class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min_number = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        if len(self.list) == 1:
            self.min_number = x
        else:
            if x < self.min_number:
                self.min_number = x

    def pop(self):
        """
        :rtype: None
        """
        if self.list:
            pop_number = self.list.pop()
            if pop_number == self.min_number and self.list:
                self.min_number = min(self.list)
            return pop_number

    def top(self):
        """
        :rtype: int
        """
        if self.list:
            return self.list[len(self.list) - 1]

    def min(self):
        """
        :rtype: int
        """
        if self.list:
            return self.min_number
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
