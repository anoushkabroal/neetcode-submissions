class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_dict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in search_dict:
                return [search_dict[difference], i]
            else:
                search_dict[nums[i]] = i

        
        return [0, 0]