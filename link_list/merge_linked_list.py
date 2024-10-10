import heapq

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_k_lists(lists):
    """
    Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted linked list.

    Args:
        lists (list_LinkedListNode_int32): A list of linked lists.

    Returns:
        LinkedListNode_int32: The merged linked list.
    """
    heap = []
    heapq.heapify(heap)
    
    for i in range(len(lists)):
        if lists[i] is not None:
            node = lists[i]
            while node is not None:
                heapq.heappush(heap, node.value)
                node = node.next
    
    dummy = LinkedListNode(None)
    tail = dummy
    
    while heap:
        value = heapq.heappop(heap)
        tail.next = LinkedListNode(value)
        tail = tail.next
    
    return dummy.next
