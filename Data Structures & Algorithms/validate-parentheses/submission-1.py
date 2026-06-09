class Solution:
    def isValid(self, s: str) -> bool:
        char_string = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in char_string:
                top_element = stack.pop() if stack else '#'
                if char_string[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
