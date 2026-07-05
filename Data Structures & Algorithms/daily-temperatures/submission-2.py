class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_i,stack_temp = stack.pop()
                res[stack_i] = i - stack_i
            
            stack.append([i,temp])
        return res