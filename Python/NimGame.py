class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True
        first, second, third = True, True, True
        flag = False
        i = 3
        while i < n:
            i += 1
            flag = not first or not second or not third
            first, second, third = second, third, flag
        return flag
      
      # or, patten
      return n%4 != 0
