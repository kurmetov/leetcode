class Solution(object):
    def findTheDifference(self, s, t):
        diff = Counter(t) - Counter(s)

        return list(diff.keys())[0]