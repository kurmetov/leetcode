class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}

        for left in range(len(nums) - k + 1):
            window = set(nums[left:left + k])

            for x in window:
                freq[x] = freq.get(x, 0) + 1

        res = -1

        for x, count in freq.items():
            if count == 1:
                res = max(res, x)

        return res