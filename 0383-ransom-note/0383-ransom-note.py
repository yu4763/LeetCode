class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        source = Counter(magazine)
        target = Counter(ransomNote)
        for t in target:
            if t not in source or source[t] < target[t]:
                return False
        
        return True
                
        