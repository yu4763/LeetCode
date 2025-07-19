class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        preserved = set()
        
        N = len(s)
        for i in range(N):
            sl = s[i]
            tl = t[i]

            if sl in map and map[sl] != tl:
                return False
            
            if sl not in map and tl in preserved:
                return False
            
            map[sl] = tl
            preserved.add(tl)

        return True
        