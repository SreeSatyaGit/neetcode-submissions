class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink window until the duplicate character is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character to set and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length