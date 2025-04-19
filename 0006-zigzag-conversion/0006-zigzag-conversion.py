class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
            
        ans = ""
        rows = [''] * numRows
        i = 0
        step = 1
        for el in s:
            rows[i] += el
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            
            i += step

        return "".join(rows)



        