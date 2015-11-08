    # loop
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            new_num = 0
            while num > 0:
                new_num += num%10
                num /= 10
            num = new_num
        return num
        
    # recursive
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num < 10 else self.addDigits(self.addHelper(num))
        
    def addHelper(self, num):
        new_num = 0
        while num > 0:
            new_num += num%10
            num /= 10
        return new_num        
