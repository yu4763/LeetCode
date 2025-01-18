class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pk = 0
        for i in range(1, len(nums)):
            if nums[pk] != nums[i]:
                pk += 1
                nums[pk] = nums[i]
        return pk + 1
                


        