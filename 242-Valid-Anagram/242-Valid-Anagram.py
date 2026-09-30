class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)

        if length_s != length_t:
            return False
        characters_s = {}
        characters_t = {}

        for i in range(length_s):
            if s[i] in characters_s:
                characters_s[s[i]] +=1
            if s[i] not in characters_s:
                characters_s[s[i]] =1
        for i in range(length_t):
            if t[i] in characters_t:
                characters_t[t[i]] +=1
            if t[i] not in characters_t:
                characters_t[t[i]] = 1
        
        if characters_s != characters_t:
            return False
        else:
            return True