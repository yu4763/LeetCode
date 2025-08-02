class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()

        def get_result(v):
            result = 0
            v, s = divmod(v, 10)
            while v > 0 or s > 0:
                result += s*s
                v, s = divmod(v, 10)
            return result

        cur = n
        while cur not in checked:
            checked.add(cur)
            cur = get_result(cur)
            if cur == 1:
                return True
        
        return False

        