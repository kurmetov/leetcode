class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ys = nums[n:]
        xs = nums[:n]
        res = []
        
        for i in range(n):

            res.append(xs[i])
            res.append(ys[i])
        

        
        return res 
