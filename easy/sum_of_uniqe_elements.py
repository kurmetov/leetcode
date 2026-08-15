class Solution(object):
    def sumOfUnique(self, nums):
        sumres = 0
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        print(seen)

        for num in nums:
            print(num)
            if seen.get(num) == 1:
                print(seen.get(num))
                sumres += num

        return sumres