class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use hashset not hashmap
        # i mean you can also solve it by sorting it but not O(n) anymore
        # create a set of nums
        hashset = set(nums)
        res = 0

        for num in hashset:
            if (num - 1) not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                res = max(length, res)
        return res
        