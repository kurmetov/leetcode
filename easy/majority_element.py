class Solution(object):
    def majorityElement(self, nums):
        seen = {}

        l = len(nums) / 2

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

            if seen.get(num) > l:
                return num

        