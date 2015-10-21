# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        stack = []
        stack.append(root)
        runner = TreeNode(-1)
        while len(stack) > 0:
            node = stack.pop()
            runner.right = node
            runner.left = None
            runner = node
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
