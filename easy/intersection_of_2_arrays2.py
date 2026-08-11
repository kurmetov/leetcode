class Solution(object):
    def intersect(self, nums1, nums2):
        results = list()
        freqs = {}

        for num in nums1:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num in nums2:
            if freqs.get(num) > 0:
                print(num)
                results.append(num)
                freqs[num] = freqs.get(num) - 1
                


        return results
        