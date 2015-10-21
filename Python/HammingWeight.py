class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            bit = 1 & n
            result += bit
            n >>= 1
        return result
