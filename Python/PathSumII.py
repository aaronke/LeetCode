# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.result = []
        self.dfs(root, sum, 0, [])
        return self.result
        
    def dfs(self, root, sum, prev_sum, prev_path):
        if root == None:
            return
        prev_path.append(root.val)
        if root.left == None and root.right == None:
            if root.val + prev_sum == sum:
                self.result.append(prev_path[:])
        self.dfs(root.left, sum, prev_sum + root.val, prev_path)
        self.dfs(root.right, sum, prev_sum + root.val, prev_path)
        del prev_path[-1]
