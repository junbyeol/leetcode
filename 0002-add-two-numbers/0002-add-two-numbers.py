# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        ans = ListNode()
        carry = 0
        p = ans

        while p1 != None or p2 != None or carry == 1:
            p.next = ListNode()
            p = p.next

            sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            carry = 1 if sum > 9 else 0

            p.val = sum % 10

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return ans.next
        