class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = [] #temp, index 
        fin = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while my_stack and temp > my_stack[-1][0]:
                stack_temp, stack_index = my_stack.pop()
                fin[stack_index] = index - stack_index
            my_stack.append((temp, index))


        return fin
