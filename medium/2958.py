class Solution(object):
    def maxSubarrayLength(self, nums, k):

        if len(nums) == 1:
            return 1

        freqs = {}
        left = 0
        lsa = 0

        for right in range(len(nums)):
            
            num = nums[right]
            freqs[num] = freqs.get(num, 0) + 1

            while freqs[num] > k:
                removed = nums[left]
                freqs[removed] -= 1
                left += 1

            current = right - left + 1
            lsa = max(lsa, current)

        return lsa


            


