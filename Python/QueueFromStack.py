class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack_out) > 0:
            self.stack_out.pop()
        else:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            self.stack_out.pop()
            

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack_out) > 0:
            return self.stack_out[-1]
        else:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
