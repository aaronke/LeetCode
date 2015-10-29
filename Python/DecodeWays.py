class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        if s[0] == '0':
            return 0
        dp = [1]*(len(s)+1)
        for i in range(2,len(s)+1):
            val = int(s[i-2:i])
            if s[i-1] == '0':
                if val == 0 or val > 26:
                    return 0
                else:
                    dp[i] = dp[i-2]
            elif val >= 11 and val <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
