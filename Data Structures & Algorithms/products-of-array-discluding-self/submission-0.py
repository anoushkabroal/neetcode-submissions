class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pref = 1
        suff = 1
        for i in range(n):
            res[i] = pref
            pref = pref*nums[i]
        for i in range(n - 1, -1, -1):
            res[i] = res[i]*suff
            suff = suff * nums[i]
        return res

