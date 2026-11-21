class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            a = asteroids[i]
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a > 0:
                    a = 0
                elif stack[-1] + a < 0:
                    stack.pop()
                else:
                    a=0
                    stack.pop()
            if a:
                stack.append(a)
        return stack