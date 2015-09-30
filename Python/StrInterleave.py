class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False
        table = [[False for j in range(n+1)] for i in range(m+1)]
        table[0][0] = True
        # init first row
        for j in range(1,n+1):
            table[0][j] = s2[j-1] == s3[j-1] and table[0][j-1]
        # initi first col
        for i in range(1,m+1):
            table[i][0] = s1[i-1] == s3[i-1] and table[i-1][0]
        # fill the table
        for i in range(1,m+1):
            for j in range(1,n+1):
                table[i][j] = s1[i-1] == s3[i+j-1] and table[i-1][j] or s2[j-1] == s3[i+j-1] and table[i][j-1]
        return table[m][n]
