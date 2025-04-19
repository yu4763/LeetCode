class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        ans = ""
        zig = [['' for _ in range(len(s))] for _ in range(numRows)]
        up = True
        i, k = 0, 0
        for el in s:
            zig[i][k] = el
            if up and i == (numRows -1):
                up = False
            elif not up and i == 0:
                up = True
            if up:
                i += 1
            else:
                i -= 1
                k += 1

        for l in zig:
            ans += "".join(l)
        return ans



        