class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if self.minStack[-1] >= x:
                self.minStack.append(x);

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]

if __name__ == "__main__":
    stack = MinStack()
    stack.push(4)
    stack.push(3)
    stack.push(1)
    stack.push(6)
    stack.push(2)
    stack.push(2)
    stack.push(3)
    print stack.top()
    print stack.getMin()
    stack.pop()
    stack.pop()
    print stack.top()
    print stack.getMin()

