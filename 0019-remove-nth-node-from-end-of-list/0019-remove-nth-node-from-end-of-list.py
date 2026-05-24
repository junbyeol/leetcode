# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = 1
        p = head
        print(p.val)
        while p.next != None:
            p = p.next
            list_size = list_size + 1
            print(p.val)

        print()

        p = head
        print(p.val)
        if list_size == n:
            return head.next

        for i in range(list_size - n - 1):
            p = p.next
            print(p.val)
        
        p.next = p.next.next

        return head
        

        