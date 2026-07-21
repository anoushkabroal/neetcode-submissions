class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        comp = set()
        
        for num in nums:
            comp.add(num)
        
        longest = 0

        for num in comp:
            if num - 1 not in comp:
                length = 1
                while num + length in comp:
                    length += 1

                longest = max(longest, length)  
        
        return longest
       
       


