# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        step = 0
        prev = node = node1 = ListNode(0, head)
        while step != n:
            prev = prev.next
            step += 1
        while prev.next:
            node = node.next
            prev = prev.next
        node.next = node.next.next
        return node1.next
