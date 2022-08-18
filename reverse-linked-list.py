# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        if  head == None  or  head.next == None: 
            return head 
        ptr1 = head.next
        ptr2  = head
        ptr2.next = None
        while ptr1.next:
            fstf = ptr1.next
            ptr1.next = ptr2
            ptr2 = ptr1
            ptr1 = fstf
        ptr1.next = ptr2
        return ptr1
