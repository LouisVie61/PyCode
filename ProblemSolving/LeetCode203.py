from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)




def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return None
    else:
        if head.val == val:
            return head.next

    prevNode = head
    curNode = prevNode.next

    while curNode is not None:
        if curNode.val == val:
            prevNode.next = curNode.next
        else:
            prevNode = curNode
        curNode = curNode.next

    return head

def rmElementsWay2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head
    preN, curN = dummy, head

    while curN:
        nextN = curN.next

        if curN.val == val:
            preN.next = nextN
        else:
            preN = curN

        curN = nextN

    return dummy.next