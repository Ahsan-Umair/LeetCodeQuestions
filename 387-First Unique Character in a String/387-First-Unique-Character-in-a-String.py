class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        length_s = len(s)

        for i in range(length_s):
            if s[i] in frequency:
                frequency[s[i]] +=1
            if s[i] not in frequency:
                frequency[s[i]] = 1
        
        for i in range(length_s):
            if frequency[s[i]] == 1:
                return i
        return -1
