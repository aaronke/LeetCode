class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        while root.left != None:
            stack.append(root)
            root = root.left
        stack.append(root)
        result = []
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right != None:
                node = node.right
                while node.left != None:
                    stack.append(node)
                    node = node.left
                stack.append(node)
        return result
