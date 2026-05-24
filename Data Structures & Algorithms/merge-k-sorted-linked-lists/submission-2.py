# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use min-heap to always find the smallest
        # to create sorted order
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for i, node in enumerate(lists):
            # python by default is min-heap
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # pop from heap 
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next: # push the next node
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

        