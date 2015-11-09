class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        codes = [0]
        for i in xrange(n):
            to_add = 1 << i
            for code in codes[::-1]:
                codes.append(code+to_add)
        return codes
