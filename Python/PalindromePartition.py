class Solution(object):
# use DP table to store which parts are palindrome
# recusive build final results by using previous results
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if n == 1:
            return [[s[0]]]
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
        result = []
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s[0]]]
        for i in range(n):
            if table[i][n-1] == True:
                pre_result = self.helper(s[:i],table)
                result += [pre+[s[i:]] for pre in pre_result]
        return result
