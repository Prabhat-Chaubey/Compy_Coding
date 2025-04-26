""""
The logic is that we will find the middle , using that as 
a pivot we would reverse the remaining half with the same
now we woud compre the both halfes and we would get to know that is is palindrome

""""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare both halves
        left = head
        right = prev  # 'prev' is the head of reversed second half
        
        while right:  # Only need to check the right part
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
