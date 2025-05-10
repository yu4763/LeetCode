class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) > len(t):
            return False

        p0, p1 = 0, 0
        while p0 < len(s) and p1 < len(t):
            if s[p0] == t[p1]:
                p0 += 1
                p1 += 1
            else:
                p1 += 1
        
        return p0 >= len(s)


        