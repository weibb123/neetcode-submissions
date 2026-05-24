# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we can dump sorted values in an array from linked list
        # then rebuild it in linked list
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        
        # step 2 sort them
        values.sort()

        # step 3 rebuild link list
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next
        