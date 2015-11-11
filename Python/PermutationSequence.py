import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [1,2,3,4,5,6,7,8,9]
        result = ''
        for i in range(n,0,-1):
            bucket_size = math.factorial(i)/i
            this_num = nums[(k-1)/bucket_size]
            del nums[(k-1)/bucket_size]
            k = (k-1)%bucket_size + 1
            result += str(this_num)
        return result
