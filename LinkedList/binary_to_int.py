# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#The best way to do so is num = num *2 + curr.val
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        curr = head
        
        while curr:
            num = num * 2 + curr.val  # Shift left and add current bit
            curr = curr.next
        
        return num
