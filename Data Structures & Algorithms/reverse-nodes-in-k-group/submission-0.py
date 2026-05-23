# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1
        
        if group == k:
            cur = self.reverseKGroup(cur, k) # cur is at node 4, for example 1->2->3->4->5, k=3
            while group > 0:
                tmp = head.next # 1 -> 2
                head.next = cur # 1->4->5, reverse part
                cur = head # went from node 4 to node 1 then node 2 then node 3
                head = tmp # 2
                group -= 1

            head = cur # 3
        return head
        