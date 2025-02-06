class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        count = [n] * n
        for i in range(n-2, -1, -1):
            if nums[i] + i  >= n-1:
                count[i] = 1
            
            else:
                jump_l = i+1
                jump_r = min(i+1+nums[i], n)
                result = min(count[jump_l:jump_r], default=0)
                if result > 0:
                    count[i] = 1 + result
        
        return count[0]
