import math, sys
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        gap = n - m
        bits = int(math.log(gap,2)) # how many bits have both '0' and '1'
        mask = 1
        while bits > 0:
            mask <<= 1
            mask += 1
            bits -= 1
        return m&n&(sys.maxint - mask) # m&n because the num between m and n will not change the result of m&n
