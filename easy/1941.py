class Solution(object):
    def areOccurrencesEqual(self, s):
        
        seen = {}
        check = {}

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        checking = list(seen.values())[0]

        for char in seen:
            if seen[char] != checking:
                return False


        return True  
            
            