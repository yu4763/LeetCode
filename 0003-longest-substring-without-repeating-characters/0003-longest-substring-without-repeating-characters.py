class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        n = len(s)
        longest = 0
        window = set()
        sub_str = ""
    
        for i in range(n):
            sub_str += s[i]
            if s[i] not in window:
                window.add(s[i])
            else:
                if longest < len(window):
                    longest = len(window)
                fi = sub_str.find(s[i])
                sub_str = sub_str[fi+1:]
                window = set(sub_str)
        
        return max(longest, len(window))



        