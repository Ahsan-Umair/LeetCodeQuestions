class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        start = 0
        answer = ""

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
        
            if count == 0:
                answer += s[start + 1:i]
                start = i + 1
        return answer