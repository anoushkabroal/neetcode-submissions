class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water_sum = 0
        while left < right:
            curr_sum = min(heights[left], heights[right]) * (right - left)
            if curr_sum > water_sum:
                water_sum = curr_sum
            
            if heights[left] < heights[right]:
                left += 1;
            else:
                right -= 1; 
        
        return water_sum