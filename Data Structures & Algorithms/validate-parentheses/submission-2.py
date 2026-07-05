class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in charMap:
                if stack and stack[-1] == charMap[char]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0