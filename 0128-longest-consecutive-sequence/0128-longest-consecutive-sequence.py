class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {key:True for key in nums}
        ans = 0
        for n in nums:
            if n-1 not in num_dict:
                cnt = 0
                cur = n
                while cur in num_dict:
                    cnt += 1
                    cur += 1
                ans = max(ans, cnt)
        
        return ans
