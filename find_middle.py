""""
The logic is that we have two pointer , 
one fast , one slow , like in the cycle detection ,
when the fast would reach the end , the slow would be in the middle

slow=slow.next
fast=fast.next.next

""""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
