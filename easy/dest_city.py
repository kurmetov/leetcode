class Solution(object):
    def destCity(self, paths):
        starts = set()

        for start, end in paths:
            starts.add(start)

        for start, end in paths:
            if end not in starts:
                return end
         

        