class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):
            smaller = 0
            for j in range(len(nums)):
                if(nums[j] < nums[i]):
                    smaller += 1

            ans.append(smaller)

        return ans