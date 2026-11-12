class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []

        def dfs(i):
            if i >= len(s):
                res.append(pal.copy())
                return
            
            for j in range(i,len(s)):
                if self.ispali(s,i,j):
                    pal.append(s[i:j+1])
                    dfs(j+1)
                    pal.pop()
        dfs(0)
        return res
    def ispali(self,s,i,j) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i,j = i+1,j-1
        return True