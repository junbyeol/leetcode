# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node가 0개 또는 1개
        if head == None or head.next == None:
            return head

        new_head = head.next

        # 첫 2개의 노드
        q = head
        r = head.next
        s = head.next.next

        r.next = q
        q.next = s

        p = q

        print(new_head)

        while p.next != None and p.next.next != None:
            print(f'p is {p.val}')
            q = p.next
            r = p.next.next
            s = p.next.next.next

            r.next = q
            q.next = s
            p.next = r

            p = q

            print(new_head)

        

        return new_head
        