#https://leetcode.com/problems/middle-of-the-linked-list/submissions/ 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        size = 0
        while fast:
            fast = fast.next
            size += 1
        mid = size // 2
        print(mid)
        while mid:
            slow = slow.next
            print(slow.val)
            mid -= 1
            print(mid)
        return slow
