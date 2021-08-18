from treenode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value=value)
        cur = self.root
        while cur.left and cur.right:
            if value > cur.value:
                cur = cur.right
            else:
                cur = cur.left

        if value > cur.value:
            cur.right = TreeNode(value)
        else:
            cur.left = TreeNode(value)
        return self

    def find(self, value):
        if not self.root:
            return False

        cur = self.root
        found = False
        while cur and found is True:
            if value > cur.value:
                cur = cur.right
            elif value < cur.value:
                cur = cur.left
            else:
                found = True
        if found is False:
            return False

        return cur

    def bfs(self):
        data = []
        queue = []
        node = self.root
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return data

    def dfs_pre(self):
        data = []
        if self.root is None:
            return []

        def helper(node):
            data.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(self.root)
        return data

    def dfs_post(self):
        data = []
        if self.root is None:
            return []

        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

            data.append(node.value)
        helper(self.root)
        return data

    def dfs_order(self):
        data = []
        if self.root is None:
            return []

        def helper(node):
            if node.left:
                helper(node.left)
            data.append(node.value)
            if node.right:
                helper(node.right)

        helper(self.root)
        return data
