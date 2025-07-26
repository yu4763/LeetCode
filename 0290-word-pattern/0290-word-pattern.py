class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        maps = dict()
        checked = set()
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in maps and maps[p] != w:
                return False
            
            if p not in maps and w in checked:
                return False
            
            maps[p] = w
            checked.add(w)
                
        
        return True

        