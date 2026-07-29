class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left >= 0 and right < len(nums):
            sum = nums[left] + nums[right] 
            if left == right:
                return [left, right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        return[left, right]