# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        stack_odd = []
        stack_even = []
        stack_odd.append(root)
        result = []
        even_level = True
        while len(stack_odd) > 0 or len(stack_even) > 0:
            this_level = []
            if even_level:
                while len(stack_odd) > 0:
                    node = stack_odd.pop()
                    this_level.append(node.val)
                    if node.left:
                        stack_even.append(node.left)
                    if node.right:
                        stack_even.append(node.right)
            else:
                while len(stack_even) > 0:
                    node = stack_even.pop()
                    this_level.append(node.val)
                    if node.right:
                        stack_odd.append(node.right)
                    if node.left:
                        stack_odd.append(node.left)
            result.append(this_level)
            even_level = not even_level
        return result
