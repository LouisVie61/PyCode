from typing import Optional

from LeetCode203 import ListNode

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next

    if list1 is not None:
        cur.next = list1
    else:
        cur.next = list2

    return dummy.next