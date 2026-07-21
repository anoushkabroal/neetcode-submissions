class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            freq_dict[sort].append(i)
        return list(freq_dict.values())
