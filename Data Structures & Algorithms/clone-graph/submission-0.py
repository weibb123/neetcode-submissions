"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {}

        def dfs_clone(node):
            # if copy already exist
            if node in old2new:
                return old2new[node]
            
            # create a copy of the node
            copy = Node(node.val)
            old2new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
            
            return copy

        
        return dfs_clone(node) if node else None
        