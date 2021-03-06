class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        if x < 2:
            return x
        left, right = 1, x/2
        while left <= right:
            mid = (left+right)/2
            if mid == x/mid:
                return mid
            elif mid < x/mid:
                left = mid + 1
            else:
                right = mid - 1
        return right
