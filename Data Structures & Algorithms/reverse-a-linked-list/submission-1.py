# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move the prev pointer forward
            current = next_node       # Move the current pointer forward
            
        return prev                   # prev will be the new head of the reversed list