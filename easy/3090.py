class Solution(object):
    def maximumLengthSubstring(self, s):
        freq = {}
        left = best = 0

        for right, x in enumerate(s):
            freq[x] = freq.get(x,0) + 1

            while freq[x] > 2:
                old = s[left]
                freq[old] -= 1
                left += 1

            best = max(best, right - left + 1)


        return best

        