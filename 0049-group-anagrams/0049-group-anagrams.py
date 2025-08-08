class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            os = ''.join(sorted(s))
            if os in result:
                result[os].append(s)
            else:
                result[os] = [s]
        return list(result.values())