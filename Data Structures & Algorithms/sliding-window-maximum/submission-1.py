class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        right = 0
        queue = collections.deque() #index

        while right < len(nums):
           while queue and nums[queue[-1]] < nums[right]: 
                queue.pop()
           queue.append(right)

           #remove left val if out of bounds
           if left > queue[0]:
            queue.popleft()
           
           if (right + 1) >= k:
            output.append(nums[queue[0]])
            left += 1
           
           right += 1

        return output