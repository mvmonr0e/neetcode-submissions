class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # contains number: index

        # iterate thru nums, tracking index
        for i, n in enumerate(nums):
            # calculate difference between target and current number
            diff = target - n

            # if the diff is in our map's keys
            if diff in prevMap:
                # return answer
                return [prevMap[diff],i]
            # else add current number and it's index to map
            prevMap[n] = i
        return []