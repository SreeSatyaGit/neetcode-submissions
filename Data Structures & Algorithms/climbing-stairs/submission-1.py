class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1

        for _ in range(n-1):
            temp = first
            first = first + second
            second = temp
        return first