# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        stack = []
        stack.append(root)
        # preorder modification, root, right, left
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return result[::-1]
