    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1]*n
        idx2, idx3, idx5 = 0, 0, 0
        for i in range(1, n):
            result[i] = min(min(2*result[idx2], 3*result[idx3]), 5*result[idx5])
            if 2*result[idx2] == result[i]:
                idx2 += 1
            if 3*result[idx3] == result[i]:
                idx3 += 1
            if 5*result[idx5] == result[i]:
                idx5 += 1                
        return result[-1]
