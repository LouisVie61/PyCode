from LeetCode203 import ListNode

def reverseLinkedList(self, head: ListNode) -> ListNode:
    if head is None:
        return None

    prev = None
    curr = head

    while curr:
        nextN = curr.next
        curr.next = prev
        prev = curr
        curr = nextN

    return prev
# 1 2 3 null

