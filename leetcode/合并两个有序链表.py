# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2) -> ListNode:
    if l1 is None:
        return l2

    if l2 is None:
        return l1





