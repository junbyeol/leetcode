# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        # 1. make cycle
        p = head # 0
        size = 1
        while p.next != None:
            p = p.next
            size = size + 1
        p.next = head

        # 2. cut off the cyle
        p = head # 0
        move_left = size - (k%size) - 1
        for i in range(0, move_left):
            p = p.next
        ans = p.next
        p.next = None

        return ans