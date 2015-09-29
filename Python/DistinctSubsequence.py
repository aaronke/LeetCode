class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if n > m or n < 1 or m < 1:
            return 0
        table = [[0 for j in range(n)] for i in range(m)]
        if s[0] == t[0]:
            table[0][0] = 1
        for i in range(1,m):
            table[i][0] = table[i-1][0] + 1 if s[i] == t[0] else table[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j]
                if s[i] == t[j]:
                    table[i][j] += table[i-1][j-1]
        return table[-1][-1]
