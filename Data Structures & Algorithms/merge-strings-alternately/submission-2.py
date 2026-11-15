class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        len1 = len(word1)
        len2 = len(word2)
        l1,l2=0,0

        while l1<len1 and l2<len2:
            res.append(word1[l1])
            res.append(word2[l2])
            l1+=1
            l2+=1
        
        res.append(word1[l1:])
        res.append(word2[l2:])
        return "".join(res)