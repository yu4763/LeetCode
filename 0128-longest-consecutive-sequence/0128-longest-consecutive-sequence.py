class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = {}
        count = {}
        for n in nums:
            if n in table:
                continue
            if n-1 in table and n+1 in table:
                prev = table[n-1]
                while prev != table[prev]:
                    prev = table[prev]
                next = table[n+1]
                while next != table[next]:
                    next = table[next]

                count[prev] += (1 + count[next])
                table[next] = prev
                table[n] = prev
            
            elif n-1 in table:
                prev = table[n-1]
                while prev != table[prev]:
                    prev = table[prev]

                count[prev] += 1
                table[n] = prev
            
            elif n+1 in table:
                next = table[n+1]
                while next != table[next]:
                    next = table[next]

                count[n] = (1 + count[next])
                table[next] = n
                table[n] = n
            
            else:
                table[n] = n
                count[n] = 1

        return max(count.values())       
