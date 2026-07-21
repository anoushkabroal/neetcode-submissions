class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for i in strs:
            the_len = len(i)
            s.append(str(the_len))
            s.append("#")
            s.append(i)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
       
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            the_len = int(s[i:j])
            i = j + 1
            ret.append(s[i:i+the_len])
            i += the_len    
        return ret