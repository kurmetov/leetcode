class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hs2 = {}
        hs1 = {}

        for char in ransomNote:
            hs1[char] = hs1.get(char, 0) + 1
        
        for char in magazine:
            hs2[char] = hs2.get(char, 0) + 1

        for char, needed_count in hs1.items():
            if hs2.get(char, 0) < needed_count:
                return False
        
        return True

