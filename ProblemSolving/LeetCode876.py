from typing import Optional
from LeetCode203 import ListNode


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    cnt = 0
    curN = head
    while curN:
        cnt += 1
        curN = curN.next

    curN = head
    mid = cnt // 2

    for i in range(mid):
        curN = curN.next

    return curN

def middleWay2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
