class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, second, result = 1, 1, 1
        for i in range(1,n):
            result = first+second
            first, second = second, result
        return result
