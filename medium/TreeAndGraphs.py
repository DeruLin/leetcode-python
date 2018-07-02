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

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, s1, e1, inorder, s2, e2):
        val = preorder[s1]
        if s1 >= e1:
            return TreeNode(val)
        index = inorder.index(val, s2, e2 + 1)
        node = TreeNode(val)
        if index != s2:
            node.left = self.helper(preorder, s1 + 1, s1 + index - s2, inorder, s2, index - 1)
        if index != e2:
            node.right = self.helper(preorder, s1 + index - s2 + 1, e1, inorder, index + 1, e2)
        return node


if __name__ == "__main__":
    preorder = [1, 2]
    inorder = [2, 1]
    solution = Solution()
    print(solution.zigzagLevelOrder(solution.buildTree(preorder, inorder)))
