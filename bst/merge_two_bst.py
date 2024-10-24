def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    # Algo: DFS, Inorder
    # trade off: time: O(N) Space O(N)
    indorder_tree1 = []
    indorder_tree2 = []
    
    def dfs(node, which_root):
        if not node: 
            return
        dfs(node.left, which_root)
        if which_root == 1:
            indorder_tree1.append(node.value)
        else:
            indorder_tree2.append(node.value)        
        dfs(node.right, which_root)
    dfs(root1, 1)
    dfs(root2, 2)
    inorder = indorder_tree1 + indorder_tree2
    inorder.sort()
    def build_bst(arr, start, end):
        if start > end:
            return None
        mid = (start + end)//2
        root = BinaryTreeNode(arr[mid])
        
        root.left = build_bst(arr, start, mid-1)
        root.right = build_bst(arr, mid + 1, end)
        return root
    
    
    return build_bst(inorder, 0, len(inorder) - 1)
