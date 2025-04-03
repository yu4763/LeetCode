class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40, 
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        result = 0
        N = len(s)
        pos = 0
        while pos < N:
            cnt = mapper.get(s[pos:pos+2], 0)
            if cnt > 0:
                pos += 2
            else:
                cnt = mapper.get(s[pos], 0)
                pos += 1
            
            result += cnt
        
        return result