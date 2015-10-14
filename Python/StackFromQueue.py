class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque        
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.popleft()
        
    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
