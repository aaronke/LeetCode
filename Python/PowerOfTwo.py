class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            bit = 1 & n
            if bit != 0:
                return False
            n >>= 1
        return n == 1
