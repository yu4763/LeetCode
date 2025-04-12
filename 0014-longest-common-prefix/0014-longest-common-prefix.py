class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        pos = 0
        while True:
            found = True
            target = ""
            for el in strs:
                if pos < len(el):
                    if not target:
                        target = el[pos]
                        continue
                    if el[pos] != target:
                        found = False
                        break
                else:
                    return prefix
            
            if found:
                prefix += target
                pos += 1
            
            else:
                return prefix


            
        