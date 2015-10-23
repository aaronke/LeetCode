# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1,n)
        
    def helper(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        result = []
        for partition in range(start,end+1):
            left_children = self.helper(start, partition-1)
            right_children = self.helper(partition+1, end)
            for left_child in left_children:
                for right_child in right_children:
                    root = TreeNode(partition)
                    root.left = left_child
                    root.right = right_child
                    result.append(root)
        return result
