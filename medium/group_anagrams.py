class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(int)
        
        for st in strs:
            key = "".join(sorted(st))

            if key not in result:
                result[key] = []

            result[key].append(st)


            
        return list(result.values())