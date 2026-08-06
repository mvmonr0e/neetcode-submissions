class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # create map
        # this map tracks each number and its index

        # iterate thru nums, tracking index
        for i, n in enumerate(nums):
            # calc difference between target and current number
            diff = target - n

            # check if difference is in our dict
            if diff in prevMap:
                # if it is return the answer
                return [prevMap[diff],i]

            # if its not in the map, add it
            prevMap[n] = i

        '''
        to complete this problem i would create a map that 
        tracks each number and it's index.

        then i would  iterate thru the list of nums
        using enumerate() to also track each num's index

        in the for loop i would calculate the difference between
        the target and the current num

        if the diff is in the map i would return the answer

        else i would add the number to the map
        '''

