class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # you can only add unique value to set

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
         