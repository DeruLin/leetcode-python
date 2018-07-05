class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


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

    def connect(self, root):
        while root and root.left:
            next_level_node = root.left
            root.left.next = root.right
            while root.next:
                root.right.next = root.next.left
                root = root.next
                root.left.next = root.right
            root = next_level_node

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        count = 0
        if root is None:
            return 0
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                stack.append(node)
                stack.append(node.left)
                node.left = None
            elif node.right is not None:
                count += 1
                if count == k:
                    return node.val
                stack.append(node.right)
                node.right = None
            else:
                count += 1
                if count == k:
                    return node.val
        return 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_len = len(grid)
        if row_len == 0:
            return 0
        col_len = len(grid[0])
        visited = [[False for i in range(col_len)] for i in range(row_len)]
        islands_count = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands_count += 1
                    self.visit(grid, i, j, visited)
        return islands_count

    def visit(self, grid, i, j, visited):
        visited[i][j] = True
        row_len = len(grid)
        col_len = len(grid[0])
        if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == "1":
            self.visit(grid, i - 1, j, visited)
        if i + 1 < row_len and not visited[i + 1][j] and grid[i + 1][j] == "1":
            self.visit(grid, i + 1, j, visited)
        if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == "1":
            self.visit(grid, i, j - 1, visited)
        if j + 1 < col_len and not visited[i][j + 1] and grid[i][j + 1] == "1":
            self.visit(grid, i, j + 1, visited)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
