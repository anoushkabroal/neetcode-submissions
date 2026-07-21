class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
           next_c = s[right]
           window[next_c] = 1 + window.get(next_c, 0)

           if next_c in countT and window[next_c] == countT[next_c]:
                have += 1

           while have == need:
            if (right - left + 1) < resLen:
                res = [left, right]
                resLen = (right - left + 1)
            window[s[left]] -= 1

            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            left += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
