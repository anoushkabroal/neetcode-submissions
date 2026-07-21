class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        max_sub = 0
        left = 0
        for r in range(len(s)):
            while s[r] in curr_set:
                curr_set.remove(s[left])
                left += 1
            curr_set.add(s[r])
            max_sub = max(max_sub, len(curr_set))
        
        return max_sub