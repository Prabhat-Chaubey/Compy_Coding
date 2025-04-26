""""
The Logic is that find the node , and replcae the link of current.next with it , 
the only edge case would be that it is the head node
so in that case we would do the self.head = current.next
""""

def Delete_a_node(self, node):
    curr = self.head
    prev = None

    while curr:
        if curr.data == node:
            if prev:  # Node is not the head
                prev.next = curr.next
            else:     # Node is the head
                self.head = curr.next
            return  # Exit after deletion
        prev = curr
        curr = curr.next
