# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lptr =rptr = head 
        if head == None:
            return head
        while rptr:
            if(head.val != rptr.val):
                head.next = rptr;
                head = head.next;
            rptr = rptr.next;
        head.next = None
        return lptr

    
    
