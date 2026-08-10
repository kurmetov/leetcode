class Solution(object):
    def uniqueOccurrences(self, arr):
        ochs = {}
        result = set()

        for num in arr:
            ochs[num] = ochs.get(num, 0) + 1

        for num in ochs.values():
            if num in result:
                return False
            
            result.add(num)

        return True
        print(ochs.values())


            


        