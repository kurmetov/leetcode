class Solution(object):
    def isIsomorphic(self, s, t):
        s_t = {}
        t_s = {}


        for a, b in zip(s, t):
            if a in s_t and s_t[a] != b:
                return False

            if b in t_s and t_s[b] != a:
                return False
            
            s_t[a] = b
            t_s[b] = a

        return True