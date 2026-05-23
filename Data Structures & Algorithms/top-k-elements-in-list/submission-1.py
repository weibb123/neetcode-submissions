class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get top K frequent elements
        # hashmap to keep occurance
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num]) # count and num
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res


        