def reverse(self,node):
    prev=None
    curr = self.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = neext_node
        
    self.head=prev
