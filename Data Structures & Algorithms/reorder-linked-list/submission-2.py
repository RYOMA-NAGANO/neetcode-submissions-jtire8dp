# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        list1, list2 = head, prev
        dummy = node = ListNode()
        while list1 and list2:
            dummy.next = list1
            dummy = dummy.next
            list1 = list1.next
            dummy.next = list2
            dummy = dummy.next
            list2 = list2.next
        if list1: dummy.next = list1
        if list2: dummy.next = list2


        