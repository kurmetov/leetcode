class Solution(object):
    def findRestaurant(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        common = {}

        for index, string in enumerate(list2):
            if string in set1:
                common[string] = index
        
        for index, string in enumerate(list1):
            if string in set2:
                common[string] = common.get(string) + index

        min_i = min(common.values())
        result = []

        for string, index_sum in common.items():
            if index_sum == min_i:
                result.append(string)
        
        return  result
       
