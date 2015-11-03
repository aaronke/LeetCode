# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use in-order seach, O(K)
# use divide and conque O(lgN*lgN)

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # divide and conque, binary search
        count = self.countNode(root.left)
        if count >= k:
            return self.kthSmallest(root.left, k)
        if count < k - 1:
            return self.kthSmallest(root.right, k-count-1)
        return root.val
        
    def countNode(self, root):
        if root is None:
            return 0
        return self.countNode(root.left)+1+self.countNode(root.right)
