class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        answer = ""

        for i in range(len(s)):
            if s[i] == '(':
                if count >0:
                    answer += s[i]
                count +=1
            if s[i] == ')':
                count -=1
                if count > 0:
                    answer += s[i]
        return answer