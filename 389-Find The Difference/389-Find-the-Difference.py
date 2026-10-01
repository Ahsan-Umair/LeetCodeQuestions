class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        frequency_s = {}
        frequency_t = {}
        length_s = len(s)
        length_t = len(t)

        for i in range(length_s):
            if s[i] in frequency_s:
                frequency_s[s[i]] +=1
            if s[i] not in frequency_s:
                frequency_s[s[i]] = 1
        
        for i in range(length_t):
            if t[i] in frequency_t:
                frequency_t[t[i]] +=1
            if t[i] not in frequency_t:
                frequency_t[t[i]] = 1
        
        for i in range(length_t):
            if t[i] not in frequency_s:
                return t[i]
            if frequency_t[t[i]] > frequency_s[t[i]]:
                return t[i]
            
        