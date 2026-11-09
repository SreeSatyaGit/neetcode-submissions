class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderind = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1] 
            
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                
                if word1[j] != word2[j]: 
                    if orderind[word2[j]] < orderind[word1[j]]:
                        return False
                    break
            else:
        
                if len(word1) > len(word2):
                    return False
                    
        return True