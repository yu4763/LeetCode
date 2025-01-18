class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import defaultdict
        counts = defaultdict(int)

        pk = 0
        for i in range(len(nums)):
            target = nums[i]
            if counts[target] < 2:
                counts[target] += 1
                nums[pk] = target
                pk += 1
        
        return pk 
        