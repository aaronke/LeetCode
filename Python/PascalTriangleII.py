    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        result = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            prev = 1
            for j in range(1, i):
                prev, result[j] = result[j], prev + result[j]
        return result
