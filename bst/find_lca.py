def lca(root, a, b):
    if not root:
        return None
        
    # If either node is root, that's the LCA
    if root.value == a.value or root.value == b.value:
        return root.value
    
    def find_lca(node):
        # Base case: reached null node
        if not node:
            return None
            
        # Found one of our target nodes
        if node.value == a.value or node.value == b.value:
            return node
            
        # Search left and right subtrees
        left = find_lca(node.left)   # Look for a or b in left subtree
        right = find_lca(node.right) # Look for a or b in right subtree
        
        # If found nodes in both subtrees, current node is LCA
        if left and right:
            return node
            
        # Return whichever subtree found a node (or None if neither did)
        return left if left else right
    
    result = find_lca(root)
    return result.value if result else None