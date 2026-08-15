class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res