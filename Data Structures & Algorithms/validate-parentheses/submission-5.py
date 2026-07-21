class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {")" : "(", "]" : "[", "}" : "{"}
    
        for c in s:
            if c in keys:
                if stack and stack[-1] == keys[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False