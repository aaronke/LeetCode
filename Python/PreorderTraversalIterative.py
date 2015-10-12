class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right != None:
                stack.append(node.right)            
            if node.left != None:
                stack.append(node.left)
        return result  
