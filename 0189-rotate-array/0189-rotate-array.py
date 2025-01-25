class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        rotated = nums[-k:] + nums[:-k]
        for i in range(len(rotated)):
            nums[i] = rotated[i]
        