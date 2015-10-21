class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result <<= 1
            mask = 1 & n
            result |= mask
            n >>= 1
        return result
