from typing import Optional, no_type_check_decorator

from LeetCode203 import ListNode

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    curN = head
    temp = None

    while curN and curN.next:
        if curN.val == curN.next.val:
            temp = curN.next.next
            curN.next = temp
        else:
            curN = curN.next

    return head
