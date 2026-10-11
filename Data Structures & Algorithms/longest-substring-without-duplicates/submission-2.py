class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxlen = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[right])
            maxlen = max(right-l + 1,maxlen)
            
        return maxlen

        