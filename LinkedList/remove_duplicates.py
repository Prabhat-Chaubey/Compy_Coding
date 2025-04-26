""""
The approach is simple when we find the duplicate
skip that node
""""

def remove_duplicates(self):
    curr = self.head
    
    while curr and curr.next:  # Check curr and curr.next both
        if curr.data == curr.next.data:
            # Skip the duplicate node
            curr.next = curr.next.next
        else:
            # Only move forward if no duplicate
            curr = curr.next
