# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pseudo = ListNode(-1)
        pseudo.next = head
        fast, slow = head, pseudo
# print(fast.val,slow.val)
        while fast:
            while fast.next and fast.val == fast.next.val:
            #duplicated
                fast = fast.next
#     no duplicate
            if slow.next == fast:
                # print(slow.next.val, fast.val)
                slow = slow.next
                fast = fast.next
#             skip the duplicate.
            else:
                slow.next = fast.next
                fast = slow.next
        return pseudo.next
        
        
        
        


