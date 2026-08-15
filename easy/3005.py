class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}
        sumres = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(list(freq.values()))

        max_freq = max(list(freq.values()))

        print(max_freq)

        for freqs in freq:
            print(freq[num])
            if freq.get(freqs) == max_freq:
                sumres += max_freq

        return sumres
            

        