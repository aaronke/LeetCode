# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# O(N) travsal and count
# O(lg^2N) binary search
# https://leetcode.com/discuss/68173/o-log-2-n-using-binary-search-python-iterative
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = self.getHeight(root)
        last_level = 0
        left, right = 0, 2**height-1
        while left <= right:
            mid = (left+right)/2
            if self.getKthNode(root, height, mid) is None:
                right = mid - 1
            else:
                left = mid + 1
                last_level = mid+1
        return last_level + 2**height - 1
        
    def getHeight(self, root):
        count = 0
        while root.left is not None:
            count += 1
            root = root.left
        return count
        
    def getKthNode(self, root, height, k):
        # binary bits representation of the root-to-leaf path
        while height > 0:
            if 2**(height-1) & k == 2**(height-1): # current bit is '1', turn right
                root = root.right
            else: # current bit is '0', turn left
                root = root.left
            height -= 1
        return root
            
