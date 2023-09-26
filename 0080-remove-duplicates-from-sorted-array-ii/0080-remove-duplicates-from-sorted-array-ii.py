class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        cur = 2
        for i in range(2, n):
            if nums[i] > nums[cur-2]:
                nums[cur] = nums[i]
                cur += 1
        
        return cur


        
        