# similar idea with PalindromeI, TLE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        table = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            table[i][i] = True
        for i in range(n-1):
            table[i][i+1] = s[i] == s[i+1]
        for j in range(2,n):
            for i in range(n-j):
                table[i][i+j] = s[i] == s[i+j] and table[i+1][i+j-1]
        result = self.helper(s,table)
        return result

    def helper(self,s,table):
        n = len(s)
        result = n
        if n == 0:
            return -1
        if n == 1:
            return 0
        for i in range(n):
            if table[i][n-1] == True:
                pre_result = self.helper(s[:i],table)
                result = min(result, pre_result+1)
        return result
