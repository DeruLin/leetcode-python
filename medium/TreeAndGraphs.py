class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        result = []
        if root is None:
            return result
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                stack.append(node)
                stack.append(node.left)
                node.left = None
            elif node.right is not None:
                result.append(node.val)
                stack.append(node.right)
                node.right = None
            else:
                result.append(node.val)
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    # root.right.right = TreeNode(1)

    print(Solution().inorderTraversal(root))
