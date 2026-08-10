class Solution(object):
    def intersection(self, nums1, nums2):
        vals = set(nums1)
        result = set()

        for num in nums2:
            if num in vals:
                result.add(num)

        return list(result)
        