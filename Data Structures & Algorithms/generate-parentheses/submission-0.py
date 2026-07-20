class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return
            
            if open_n < n:
                stack.append("(")
                dfs(open_n+1,closed_n)
                stack.pop()
            
            if closed_n < open_n:
                stack.append(")")
                dfs(open_n,closed_n+1)
                stack.pop()
        dfs(0,0)
        return res