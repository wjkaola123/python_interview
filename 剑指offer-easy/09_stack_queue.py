class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        :param data:  int
        :return:
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数
        :return:
        """
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.stack == []

    def peek(self):
        """
        取栈顶元素
        :return:
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None


class CQueue(object):

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        return self.stack_in.push(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack_out.is_empty():
            return self.stack_out.pop()

        if self.stack_in.is_empty():
            return -1

        while not self.stack_in.is_empty():
            self.stack_out.push(self.stack_in.pop())

        return self.stack_out.pop()


if __name__ == '__main__':
    pass
