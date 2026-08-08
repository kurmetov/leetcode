class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], index]
            
            seen[num] = index