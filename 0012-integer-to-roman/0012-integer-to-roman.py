class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        def add_result(start, size, s1, s5, s10):
            if size == 9:
                start = start + s1 + s10
            elif size == 4:
                start = start + s1 + s5
            elif size < 5:
                start  = start + (s1 * size)
            else:
                start = start + s5 + (s1 * (size-5))
            
            return start
    

        result = ''
        m, num = divmod(num, 1000)
        result += 'M' * m

        c, num = divmod(num, 100)
        result = add_result(result, c, 'C', 'D', 'M')

        x, num = divmod(num, 10)
        result = add_result(result, x, 'X', 'L', 'C')

        result = add_result(result, num, 'I', 'V', 'X')

        return result


    
        