class Solution(object):
    def wordPattern(self, pattern, s):
        p_s = {}
        s_p = {}

        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for pattern, word in zip(pattern, words):
            print(pattern, word)
            if pattern in p_s and p_s[pattern] != word:
                return False

            if word in s_p and s_p[word] != pattern:
                return False
            
            p_s[pattern] = word
            s_p[word] = pattern

        return True