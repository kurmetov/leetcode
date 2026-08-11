class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j_s = set(jewels)
        counter = 0
        

        for stone in stones:
            if stone in j_s:
                counter += 1
            
        return counter