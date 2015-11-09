    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        result = [[1]]
        for i in range(1,numRows):
            thisRow = [1]
            for j in range(1, i):
                thisRow.append(result[i-1][j-1] + result[i-1][j])
            thisRow.append(1)
            result.append(thisRow)
        return result
