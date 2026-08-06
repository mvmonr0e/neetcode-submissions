class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        # assign counts for each num
        for num in nums:
            count[num] = 1 + count.get(num,0)

        # place a num in freq
        # this number's position will be its count
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # create result by iterating thru buckets backwards
        # remember there is only on number in each bucket
        # we go backwards bc if a numbers position is higher then
        # it is more frequent
        result = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
        
        
