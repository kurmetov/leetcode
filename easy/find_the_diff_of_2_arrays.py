class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        answer1 = []
        answer2 = []
        
        for num in nums1_s:
            if num not in nums2_s:
                answer1.append(num)

        for num in nums2_s:
            if num not in nums1_s:
                answer2.append(num)
        

        return [answer1, answer2 ]