from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1. Reach node at position `left` (`cur`) and track its predecessor (`leftprev`)
        leftprev, cur = dummy, head
        for _ in range(left - 1):
            leftprev, cur = cur, cur.next

        # 2. Reverse nodes from `left` to `right` (`right - left + 1` nodes)
        prev = None
        for _ in range(right - left + 1):
            tempnext = cur.next
            cur.next = prev
            prev, cur = cur, tempnext

        # 3. Reconnect reversed sublist back to the rest of the list
        # `leftprev.next` is the original `left` node (now the tail of the reversed segment)
        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next