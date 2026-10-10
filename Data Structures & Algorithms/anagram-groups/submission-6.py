class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sorted_key = "".join(sorted(string))
            if sorted_key not in hashmap:
                hashmap[sorted_key] = []
            hashmap[sorted_key].append(string)
        
        return list(hashmap.values())