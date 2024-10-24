rom collections import deque

def find_maximum_width(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0
    
    # Use queue to store (node, position) pairs
    # Position helps track gaps in each level
    queue = deque([(root, 0)])
    max_width = 0
    
    while queue:
        level_size = len(queue)
        # Get left and right most positions in current level
        left_pos = queue[0][1]  # Position of leftmost node
        right_pos = queue[-1][1]  # Position of rightmost node
        
        # Update max width by including gaps
        max_width = max(max_width, right_pos - left_pos + 1)
        
        # Process current level
        for _ in range(level_size):
            node, position = queue.popleft()
            
            # For left child: 2 * position
            if node.left:
                queue.append((node.left, position * 2))
                
            # For right child: 2 * position + 1
            if node.right:
                queue.append((node.right, position * 2 + 1))
    
    return max_width