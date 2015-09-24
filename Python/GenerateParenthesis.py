# recursive DP
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # dp, f(n) = '(f(0))'+ f(n-1)
        #           + '(f(1))' + f(n-2)
        #           + '(f(2))' + f(n-3)
        #           + '(f(n-1))' + f(0)
        if n == 0:
            return ['']
        result = []
        for i in range(n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-1-i)
            for left_i in left:
                for right_i in right:
                    result.append('(' + left_i + ')' + right_i)
        return result

# store DP results in 2d list        
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_all = [['']]
        for i in range(1,n+1):
            result_this = []
            for j in range(i):
                for e in  result_all[j]:
                    for f in result_all[i - j - 1]:
                        result_this.append('('+ e +')' + f)
            result_all.append(result_this)
        return result_all[-1]
