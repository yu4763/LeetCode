class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        for i, n in enumerate(nums):
            if n in index:
                pi = index[n]
                if i - pi <= k:
                    return True
            
            index[n] = i
        
        return False
        