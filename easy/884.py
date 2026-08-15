class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        uncommon = []
        split1 = s1.split(" ")
        split2 = s2.split(" ")

        freq1 = Counter(split1)
        freq2 = Counter(split2)
        print(freq1["apple"])

        for word in split1:
            
            if word not in freq2 and not freq1[word] > 1:
                uncommon.append(word)

        for word in split2:
            if word not in freq1 and not freq2[word] > 1:
                uncommon.append(word)


        return uncommon