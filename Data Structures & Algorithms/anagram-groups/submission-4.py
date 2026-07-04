class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] +=1

            wordmap[tuple(count)].append(word)
        return list(wordmap.values())