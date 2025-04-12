class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        
        min_length = min(len(first), len(last))
        for i in range(min_length):
            if (first[i] != last[i]):
                return prefix
            prefix += first[i]
        
        return prefix