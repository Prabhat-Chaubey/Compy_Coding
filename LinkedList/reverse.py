def reverse(self,node):
    prev=None
    curr = self.head
    while curr:
        next_node = curr.next  #stroing the value 1 -> 2 -> 3 , so this would store 3 , as we want to move to three in next step
        curr.next = prev      # since the curr is at 2 , now its reversing 1 -> 2 to 2 -> 1
        prev = curr          # now we are update the previous , from 1 to 2, so this can keep on working
        curr = neext_node    # moving the curr node from 2 to 3
        
    self.head=prev
