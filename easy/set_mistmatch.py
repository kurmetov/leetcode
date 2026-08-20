class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s1 = set()
        duplicate = 0

        for num in nums:
            if num in s1:
                duplicate = num
            
            s1.add(num)
        missing = 0

        
        for num in range(1, len(nums) + 1):
            if num not in s1:
                missing = num
                break

        return [duplicate, missing]