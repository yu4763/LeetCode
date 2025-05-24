class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        def get_next(ordered, i, step):
            cand = i + step
            if cand < 0 or cand >= len(ordered):
                return cand
            if ordered[cand] == ordered[i]:
                return get_next(ordered, cand, step)    
            else:
                return cand

        ordered = sorted(nums)
        N = len(nums)
        result = []
        for i in range(N):
            if i > 0 and ordered[i] == ordered[i-1]: 
                continue

            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                current = ordered[i] + ordered[p1] + ordered[p2]
                if current == 0:
                    result.append([ordered[i], ordered[p1], ordered[p2]])
                    p1 = get_next(ordered, p1, 1)
                elif current < 0:
                    p1 = get_next(ordered, p1, 1)
                else:
                    p2 = get_next(ordered, p2, -1)
        return result


        