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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack1 = []
        stack2 = []
        result = []
        temp = []
        turn = True  # 先拿左边，再拿右边
        if root is None:
            return result
        stack1.append(root)
        while True:
            if turn:
                node = stack1.pop()
                temp.append(node.val)
                if node.left is not None:
                    stack2.append(node.left)
                if node.right is not None:
                    stack2.append(node.right)
            if not turn:
                node = stack2.pop()
                temp.append(node.val)
                if node.right is not None:
                    stack1.append(node.right)
                if node.left is not None:
                    stack1.append(node.left)
            if turn and len(stack1) == 0:
                turn = False
                result.append(temp.copy())
                temp.clear()
            elif not turn and len(stack2) == 0:
                turn = True
                result.append(temp.copy())
                temp.clear()
            if len(stack1) == 0 and len(stack2) == 0:
                break
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(7)
    # root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)
    # root.right.right = TreeNode(1)

    print(Solution().zigzagLevelOrder(root))
