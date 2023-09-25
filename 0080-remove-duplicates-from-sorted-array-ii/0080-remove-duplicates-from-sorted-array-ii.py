class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        dupl = 0
        prev = nums[0]
        removed = 0
        for i, n in enumerate(nums):
            if n == prev:
                dupl += 1
                if dupl >= 3:
                    nums[i] = float("inf")
                    removed += 1
            else:
                prev = n
                dupl = 1

        for i in range(1, len(nums)):
            si = i
            while nums[si] < nums[si-1]:
                nums[si], nums[si-1] = nums[si-1], nums[si]
                si -= 1

        return len(nums) - removed

        
        