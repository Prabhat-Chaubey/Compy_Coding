#The logic is we move with two pointers, one slow and one fast, if the fast one meets the slow 
#This means that there was a cycle in the linked list
def isCyclic(self):
    slow = self.head
    fast = self.head
    
    while fast and fast.next:  #This checks the condtition that fast and fast.next is possible
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
