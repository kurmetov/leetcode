class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for index, num in enumerate(nums):
            if num in seen:
                if abs(seen.get(num) - index) <= k:
                    print(num, index)
                    print(seen.get(num) - index)
                    return True
            
            seen[num] = index

        
        return False