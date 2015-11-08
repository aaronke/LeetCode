    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # recursive
        if s is None or len(s) < 1:
            return 0
        return self.titleToNumber(s[:-1])*26 + ord(s[-1])-ord('A')+1
        
        num = 0
        for c in s:
            num = 26*num + ord(c)-ord('A')+1
        return num        
