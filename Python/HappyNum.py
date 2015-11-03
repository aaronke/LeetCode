class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = abs(n)
        loop_check = set()
        while True:
            new_n = 0
            while n > 0:
                new_n += (n%10)*(n%10)
                n = n/10
            if new_n in loop_check:
                return False
            if new_n == 1:
                return True
            loop_check.add(new_n)
            n = new_n
