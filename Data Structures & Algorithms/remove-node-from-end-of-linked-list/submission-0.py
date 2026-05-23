# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers kinda like slow and fast pointer

        dummy = ListNode(0, head)
        left, right = dummy, head

        # locate the value at index = n
        while n > 0:
            right = right.next
            n -=1
        
        # move right pointer until .next -> null
        # move left pointer to the value before n
        while right:
            right = right.next
            left = left.next
        
        # update connection to skip over deleted node
        left.next = left.next.next
        return dummy.next

        