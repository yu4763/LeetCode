class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      numMaps = {}
      n = len(nums)
      
      for i in range(n):
        numMaps[nums[i]] = i
      
      for i in range(n):
        complement = target - nums[i]
        if complement in numMaps and numMaps[complement] != i:
          return [i, numMaps[complement]]


        