class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        needs = 1
        possible = True
        for i in range(n-2, -1, -1):
            if nums[i] < needs:
                needs += 1
                possible = False
            if nums[i] >= needs:
                needs = 1
                possible = True
        return possible
            
            


