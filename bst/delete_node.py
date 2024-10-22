from .tree_node import TreeNode


def delete_node(node: TreeNode, value: int):
    cur, prev = node, None
    while cur and cur.value != value:
        prev = cur
        if value > cur.value:
            cur = cur.right
        else:
            cur = cur.left
    if not cur: return node
        # case 1 node is a leaf
    if not cur.left and not cur.right:
        if prev:
            if cur == prev.left:
                prev.left = None
            if cur == prev.right:
                prev.right = None
        else:
            return None
        # case 2 node has one child:
    elif cur.left and not cur.right:
        if not prev:
            return cur.left
        if prev.left == cur:
            prev.left = cur.left
        else:
            prev.right = cur.left
    elif cur.right and not cur.left:
        if not prev: return cur.right
        if cur == prev.left:
            prev.left = cur.right
        if cur == prev.right:
            prev.right = cur.right
        # case 3 node has two children
    else:
        prev = cur
        succ = cur.right
        while succ.left:
            prev = succ
            succ = succ.left
        cur.value = succ.value
        if succ == prev.left:
            prev.left = succ.right
        else:
            prev.right = succ.right
    return node

def delete_from_bst(root: TreeNode, values_to_be_deleted: list):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    
    for i in values_to_be_deleted:
        root = delete_node(root, i)
        
            
    return root

# would sorting helps?
# BST Deletion Process: The deletion process in a binary search tree (BST) involves:

#Searching for the node to delete.
#Rearranging the tree based on the node's children.
#These operations are independent of the order in which you delete the nodes. Each deletion is handled in isolation, meaning deleting nodes in sorted order won't affect the time it takes to search for and delete individual nodes.