class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0
        self.search([],n)
        return self.result
    
    def search(self, cols, n):
        if len(cols) == n:
            self.result += 1
            return
        for i in range(n):
            if i in cols:
                continue
            cols.append(i)
            if self.isValid(cols):
                self.search(cols,n)
            del cols[-1]
    
    def isValid(self, cols):
        for i in range(len(cols)-1):
            for j in range(i+1, len(cols)):
                if cols[j] == cols[i]+j-i or cols[j] == cols[i]-j+i:
                    return False
        return True
