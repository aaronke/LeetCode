# DP,merge the min leaf of the parent to one point, bottem up
def minimumTotal(self, triangle):
    dp = [0]*len(triangle)
    for row in xrange(len(triangle)-1,-1,-1):
        for i in xrange(len(triangle[row])):
            dp[i] += triangle[row][i]
        for i in xrange(len(triangle[row])-1):
            dp[i] = min(dp[i], dp[i+1])
    return dp[0]

# DFS, like a tree
def minimumTotal(self, triangle):
    if triangle is None or len(triangle) < 1:
        return 0
    return self.dfs(triangle, 0, 0)

def dfs(self, triangle, level, idx):
    if level == len(triangle)-1:
        return triangle[level][idx]
    return triangle[level][idx] + min(self.dfs(triangle, level+1, idx), self.dfs(triangle, level+1, idx+1))
