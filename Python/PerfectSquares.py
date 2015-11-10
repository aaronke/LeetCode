def numSquares(self, n):
    # O(N^2), scan from 0 to i-1 for n times
    import math
    dp = [n]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(i):
            if int(math.sqrt(i-j))**2 == i-j:
                dp[i] = min(dp[i], dp[j]+1)
    return dp[-1]
    
    # O(N*lgN) version, set from lower dp, ealry stop    
    for i in range(0,n):
        j = 1
        while i + j*j <= n:
            dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
            j += 1    
