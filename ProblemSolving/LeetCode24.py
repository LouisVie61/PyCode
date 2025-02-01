from typing import Optional

from LeetCode203 import ListNode

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    dummy = ListNode(-1)
    preNode = dummy
    curNode = head

    while curNode and curNode.next:
        # Identify the swap nodes
        firstNode = curNode
        secondNode  = curNode.next

        # Swap operations
        preNode.next = secondNode
        firstNode.next = secondNode.next
        secondNode.next = firstNode

        # Move to the next swap
        preNode = firstNode
        curNode = firstNode.next

    return dummy.next