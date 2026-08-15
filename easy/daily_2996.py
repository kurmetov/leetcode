class Solution(object):
    def missingInteger(self, nums):   
        seen = {}
        tsum = 0

        for index, num in enumerate(nums):
            seen[index] = num
        

        if len(nums) == 1:
            tsum += nums[0] + 1
            return tsum

        if nums[0] + 1 != nums[1]:
            tsum += nums[0] + 1

        for index in seen:
            if index == 0 and seen[index] + 1 == seen[index + 1]:
                tsum += seen[index]
                continue
                
            
            if index != 0 and seen[index] == seen[index - 1] + 1:
                tsum += seen[index]
            else:
                break
            
        seen_s = sorted(seen.values())
        while(tsum in seen_s):
            tsum += 1

        return tsum