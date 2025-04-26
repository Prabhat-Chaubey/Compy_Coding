def merge_sort(self, node1, node2):
    dummy = ListNode(0)  # Step 1: Create a dummy node
    tail = dummy         # Step 2: Tail points to dummy

    # Step 3: Compare nodes and build list
    while node1 and node2:
        if node1.val < node2.val:
            tail.next = node1   # Attach node1 to merged list
            node1 = node1.next  # Move node1 ahead
        else:
            tail.next = node2   # Attach node2 to merged list
            node2 = node2.next  # Move node2 ahead
        tail = tail.next        # Move tail ahead

    # Step 4: Attach any leftover nodes
    if node1:
        tail.next = node1
    if node2:
        tail.next = node2

    return dummy.next  # Step 5: Return head of merged list
