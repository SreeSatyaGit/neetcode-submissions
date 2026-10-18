class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bMap = {"]":"[","}":"{",")":"("}

        for c in s:
            if c in bMap:
                if stack and stack[-1] == bMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False       
                