class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, p, z = [], [], []
        result = set()
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
        
        p_set = set(p)
        n_set = set(n)

        if z:
            if len(z) >= 3:
                result.add((0, 0, 0))
            for num in p:
                if -num in n_set:
                    result.add((-num, 0, num))
        
        for i in range(len(n)):
            for k in range(i+1, len(n)):
                target = -1*(n[i]+n[k])
                if target in p_set:
                    result.add(tuple(sorted([n[i], n[k], target])))
        
        for i in range(len(p)):
            for k in range(i+1, len(p)):
                target = -1*(p[i]+p[k])
                if target in n_set:
                    result.add(tuple(sorted([p[i], p[k], target])))
        
        return result
        
        